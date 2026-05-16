import streamlit as st
import pandas as pd
import time
import numpy as np

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

def format_val(val, is_ratio):
    if is_ratio:
        return f"{val:.2f}%"
    else:
        return f"{val:,.2f}"

def color_variance(val):
    if val > 0:
        return "color: green"
    elif val < 0:
        return "color: red"
    else:
        return "color: black"

display = combined[["line_item","section", col_a,col_b,"Var","Var%","is_ratio"]].copy()

for col in [col_a, col_b, "Var", "Var%"]:
    display[col] = display.apply(
        lambda r: format_val(r[col], r["is_ratio"]), axis=1
    )

display["Var%"] = pd.to_numeric(display["Var%"], errors='coerce')
display["Var%"] = display["Var%"].apply(lambda x: f'{x:+.1f}%')


display = display.drop(columns=["is_ratio"])

##### PAGE PRINCIPALE #####

st.write(f"LoB: **{lob}** . Mode: **{mode}**")
st.write(f"Comparing: **{label_a}**  vs  **{label_b}**")
st.write(f"Period: **{label_c}**")


tab1, tab2, tab3 = st.tabs(["Overview", "Detailed Analysis", "Raw Data"])

with tab1:
    st.caption(f"Overview: {lob} . {col_a}  vs  {col_b}")

    # st.divider() 
    
    col1, col2, col3 = st.columns (3)

    with col1: 
        st.metric(f"{display['line_item'][2]} {col_b}", display[col_b][2], display["Var%"][2])
        st.caption(f"Variance in %")
    with col2:
        st.metric(f"{display['line_item'][29]} {col_b}", display[col_b][29], display["Var"][29])
        st.caption(f"Variance in ppts")
    with col3:
        st.metric(f"{display['line_item'][34]} {col_b}", display[col_b][34], display["Var"][34])
        st.caption(f"Variance in ppts")

    st.divider()

    st.dataframe(
        display,
        use_container_width=True,
        hide_index=True
    )
with tab2:
    st.write("Detailed Analysis")

with tab3:
    st.write("Raw Data")
    if df is not None:
        st.write(df)