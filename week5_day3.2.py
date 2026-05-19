import streamlit as st
import pandas as pd
import time
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="GPM Financial Analysis", layout="wide")

st.title("GPM Financial Analysis")
st.write("This is a simple app for financial analysis. please refer to the guidebook if you have any questions.")

##### LOAD DATA #####

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df



def load_uploaded_file(uploaded_file):
    return pd.read_csv(uploaded_file)

df = load_data("axa_pnl_long.csv")

##### MENU / SIDEBAR #####
with st.sidebar:
    st.header("Controls MENU")
    st.write("Use the controls below to interact with the data :)")

    st.divider()


    st.header("➕ Upload Data")
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        st.warning("File upload doesn't work yet!")

    st.divider()
    st.header("Comparison Mode")
    mode = st.radio("Comparison type", ["Version", "Period"])

    if mode == "Version":
        period = st.selectbox("Period (fixed)", sorted(df["period"].unique()))
        col1, col2 = st.columns(2)
        with col1:
            version_a = st.selectbox("Version A", sorted(df["version"].unique()))
            year_a = st.selectbox("Year A", sorted(df["year"].unique()), index=1)
        with col2:
            version_b = st.selectbox("Version B", sorted(df["version"].unique()))
            year_b = st.selectbox("Year B", sorted(df["year"].unique()), index=1)
        lob = st.selectbox("LoB",sorted(df["lob"].unique()))
        label_a, label_b, label_c, label_d, label_e = version_a, version_b, period, year_a, year_b
        if version_a == version_b:
            st.warning("Please select different versions for comparison.")
    else:
        version = st.selectbox("Version (fixed)", sorted(df["version"].unique()))
        year = st.selectbox("Year", sorted(df["year"].unique()), index=1)
        period_a = st.selectbox("Period A", sorted(df["period"].unique()))
        period_b = st.selectbox("Period B", sorted(df["period"].unique()))
        lob = st.selectbox("LoB",sorted(df["lob"].unique()))
        label_a, label_b, label_c, label_d = period_a, period_b, version, year
        if period_a == period_b:
            st.warning("Please select different periods for comparison.")

##### FILTER FUNCTION / COMP TABLE #####
def get_slice(df, version, period, lob, year):

    return(
        df[(df["year"] == year) &
            (df["version"] == version) &
            (df["period"] == period) &
            (df["lob"] == lob)]
        .set_index("line_item")[["value","is_ratio","sort_order","section","is_subtotal"]]
    )       

if mode == "Version":
    slice_a = get_slice(df, version_a, period, lob, year_a)
    slice_b = get_slice(df, version_b, period, lob, year_b)
    col_a, col_b = version_a, version_b
else:
    slice_a = get_slice(df, version, period_a, lob, year)
    slice_b = get_slice(df, version, period_b, lob, year)
    col_a, col_b = period_a, period_b   

combined = slice_a[["value","is_ratio","sort_order","section","is_subtotal"]].copy()
combined.columns = [col_a,"is_ratio","sort_order","section","is_subtotal"]
combined[col_b] = slice_b["value"]
combined["Var"] = combined[col_b] - combined[col_a]
combined["Var%"] = ((combined["Var"] / combined[col_a]) * 100).round(2)
combined = combined.sort_values("sort_order").reset_index()

def get_metric(df, line_name, value_col):
    rows = df[df["line_item"] == line_name]
    if rows.empty:
        return None, None, None
    row = rows.iloc[0]
    return row[value_col], row["Var"], row["Var%"]

gep_b, gep_var, gep_var_pct = get_metric(combined, "GEP", col_b)
chc_ratio_b, chc_ratio_var, chc_ratio_var_pct = get_metric(combined, "CHC Ratio", col_b)
ecr_b, ecr_var, ecr_var_pct = get_metric(combined, "ECR", col_b)

def fmt(val, is_ratio):
    if pd.isna(val):
        return "-"
    if is_ratio:
        return f"{val:.2f}%"
    return f"{val:,.2f}"

def fmt_var(val, is_ratio):
    if pd.isna(val):
        return "-"
    if is_ratio:
        return f"{val:+.2f}ppts"
    return f"{val:+,.2f}"

def fmt_varp(val, is_ratio):
    if pd.isna(val):
        return "-"
    return f"{val:+,.2f}%"


display = combined[["line_item","section", "is_ratio", col_a,col_b,"Var","Var%"]].copy()

for col in [col_a, col_b]:
    display[col] = display.apply(
        lambda r: fmt(r[col], r["is_ratio"]), axis=1
    )

display["Var"] = display.apply(lambda r: fmt_var(r["Var"], r["is_ratio"]), axis=1)
display["Var%"] = display.apply(lambda r: fmt_varp(r["Var%"], r["is_ratio"]), axis=1)


display = display.drop(columns=["is_ratio"])

##### VAR CHART 1 #####

   
chart_df = combined[combined["is_ratio"]==False].copy()
fig = px.bar(
    chart_df,
    x="line_item",
    y="Var",
    color="section",
    title=f"{col_b} Delta vs {col_a} by Section"
)
fig.update_layout(xaxis_tickangle=-45,showlegend=True)


##### VAR CHART 2 #####
combined2 = combined.copy()
for row in combined2["line_item"].unique():
    if not (row == "GEP" or row == "Claims Handling costs" or row == "Non-Commission expenses" or row == "Total ECR"):
        combined2 = combined2[combined2["line_item"] != row]


fig2 = px.bar(
    combined2,
    x="line_item",
    y=col_b,
    color="section",
    title=f"{col_b} by Section"
)
fig2.update_layout(xaxis_tickangle=-45,showlegend=True)
##### WATERFALL CHART 1 #####
fig_w = go.Figure(go.Waterfall(
    name        = "2025",
    orientation = "v",                          # vertical bars
    measure     = ["absolute",                  # starting bar
                "relative",                  # goes up/down
                "absolute",
                "relative",
                "relative",
                "total"],                    # final sum bar
    x           = ["Revenue", "Claims", "Technical Result","NCE", "CHC", "UE"],
    y           = [500000,    -150000, 350000, -50000,  -30000,  270000],
    text        = ["+500K", "-150K", "+350K", "-50K", "-30K", "270K"],
    textposition= "outside",
    connector   = {"line": {"color": "rgb(63, 63, 63)"}},  # lines between bars
))

fig_w.update_layout(
title       = f"Profit Waterfall {col_b} - {year_b}",
showlegend  = True,
height      = 500,
)

##### WATERFALL CHART 2 #####


fig_w2 = go.Figure(go.Waterfall(
name        = "2025v2",
orientation = "v",                          # vertical bars
measure     = ["absolute",                  # starting bar
            "relative",                  # goes up/down
            "absolute",
            "relative",
            "relative",
            "total"],                    # final sum bar
x           = ["Revenue", "Claims", "Technical Result","NCE", "CHC", "UE"],
y           = [500000,    -150000, 350000, -50000,  -30000,  270000],
text        = ["+500K", "-150K", "+350K", "-50K", "-30K", "270K"],
textposition= "outside",
connector   = {"line": {"color": "rgb(63, 63, 63)"}},  # lines between bars
))

fig_w2.update_layout(
title       = f"Profit Waterfall {col_b} - {year_b}",
showlegend  = True,
height      = 500,
)

###########################
##### PAGE PRINCIPALE #####
###########################




st.write(f"LoB: **{lob}** . Mode: **{mode}**")
st.write(f"Comparing: **{label_a}**  vs  **{label_b}**")
st.write(f"Period: **{label_c}**")


tab1, tab2, tab3 = st.tabs(["Overview", "Detailed Analysis", "Raw Data"])

with tab1:
    st.caption(f"Overview: {lob} . {col_a}  vs  {col_b}")

    # st.divider() 
    
    col1, col2, col3 = st.columns (3)

    with col1: 
        st.metric(
            label=f"{display['line_item'][2]} {col_b}",
            value=display[col_b][2],
            delta=display["Var%"][2]
        )
    with col2:
        st.metric(f"{display['line_item'][29]} {col_b}", display[col_b][29], display["Var"][29])

    with col3:
        st.metric(f"{display['line_item'][34]} {col_b}", display[col_b][34], display["Var"][34])


    st.divider()
    st.subheader(f"{col_b} by Section")
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()
    st.subheader("Variance by Line")
    st.caption("Please click in legend on the sections you want to view")
    st.plotly_chart(fig, use_container_width=True)
    
    
    st.divider()
    st.subheader("Data Summary")
    st.dataframe(
        display.style.applymap(
            lambda v: "color: green" if "+" in str(v) else "color: red" if "-" in str(v) else "color: black",
            subset=["Var%"]
        ),
        use_container_width=True,
        hide_index=True
    )
with tab2:
    st.write("Detailed Analysis")



    st.plotly_chart(fig_w, use_container_width=True)

    st.divider()



    st.plotly_chart(fig_w2, use_container_width=True)




with tab3:
    st.write("Raw Data")
    if df is not None:
        st.write(df)