import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Work Shift Scheduler", layout="wide")

st.title("📅 Work Shift Scheduler")

# Initialize session state for shifts data
if 'shifts' not in st.session_state:
    st.session_state.shifts = pd.DataFrame(columns=['Date', 'Person', 'Shift', 'Status'])

# Sidebar for adding shifts
with st.sidebar:
    st.header("Add New Shift")
    shift_date = st.date_input("Select Date")
    person_name = st.text_input("Employee Name")
    shift_type = st.selectbox("Shift Type", ["Morning (6AM-2PM)", "Afternoon (2PM-10PM)", "Night (10PM-6AM)"])
    status = st.selectbox("Status", ["Scheduled", "Confirmed", "Cancelled"])
    
    if st.button("Add Shift"):
        new_shift = pd.DataFrame({
            'Date': [shift_date],
            'Person': [person_name],
            'Shift': [shift_type],
            'Status': [status]
        })
        st.session_state.shifts = pd.concat([st.session_state.shifts, new_shift], ignore_index=True)
        st.success("Shift added!")

# Main display
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Schedule")
    if not st.session_state.shifts.empty:
        st.dataframe(st.session_state.shifts, use_container_width=True)
    else:
        st.info("No shifts scheduled yet")

with col2:
    st.subheader("Stats")
    if not st.session_state.shifts.empty:
        st.metric("Total Shifts", len(st.session_state.shifts))
        st.metric("Employees", st.session_state.shifts['Person'].nunique())

# Clear all shifts button
if st.button("Clear All Shifts"):
    st.session_state.shifts = pd.DataFrame(columns=['Date', 'Person', 'Shift', 'Status'])
    st.rerun()