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
        year = st.slider('Please select the year or years you wish to inspect',2024,2030,(2025,2026))
        period_a = st.selectbox("Period A", sorted(df["period"].unique()))
        period_b = st.selectbox("Period B", sorted(df["period"].unique()))
        lob = st.selectbox("LoB",sorted(df["lob"].unique()))
        label_a, label_b, label_c, label_d = period_a, period_b, version, year
        if period_a == period_b:
            st.warning("Please select different periods for comparison.")



##### PAGE PRINCIPALE #####

st.write(f"LoB: **{lob}** . Mode: **{mode}**")
st.write(f"Comparing: **{label_a}**  vs  **{label_b}**")
st.write(f"Period: **{label_c}**")
