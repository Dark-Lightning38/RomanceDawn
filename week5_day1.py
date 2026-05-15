import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import time
from io import StringIO



st.set_page_config(page_title="GPM Financial Analysis", layout="wide")

st.title("GPM Financial Analysis")
st.write("This is a simple app for financial analysis. please refer to the guidebook if you have any questions.")

def PeriodComp():
    
    with st.sidebar:
        st.header("➕ Menu")
   
    st.divider()

    @st.cache_data
    def load_data():
        # Simulate a slow data loading operation
        time.sleep(1)
        return pd.DataFrame(np.random.randn(10, 20), columns=[f'col {i}' for i in range(20)])

    df = load_data()

    st.divider()

    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")

   
    st.divider()
    
    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'

def VersionComp():
    st.divider()
    desire = st.text_input("Would you rather compare versions or periods of P&L ?")

    st.divider()

    tab1, tab2 = st.tabs(["Version Comparison","Period Comparison"])

    with tab1:
        st.write("Version Comparison will go here")

    with tab2:
        st.write("Period Comparison will go here")

    st.divider()


    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))

    st.divider()
    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

    df #magic in place no need to use write AHAHHA

    st.divider()
    dataframe = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20)))

    st.dataframe(dataframe.style.highlight_max(axis=0)) #interesting styling choice......

    st.divider()
    x = st.slider('Please select the year or years you wish to inspect',2024,2030,(2025,2026))  # 👈 this is a widget

    st.divider()
    appointment = st.slider(
        "Schedule your appointment:", value=(time(11, 30), time(12, 45))
    )
    st.write("You're scheduled for:", appointment)


    st.text_input("Your name", key="name")

    # You can access the value at any point with:
    st.session_state.name

    if st.checkbox('Show dataframe'): #Shows only if ticked... cool
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        chart_data


    df2 = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })

    option = st.selectbox(
        'Which number do you like best?', #this goes with df2 column as chocies.... interesting
        df2['first column'])

    'You selected: ', option

def widgettest():
    
    st.title("Loading Example with Spinner")

    @st.cache_data  # 👈 Add the caching decorator
    def load_data(url):
        df = pd.read_csv(url)
        return df

    df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
    st.dataframe(df)

    st.button("Rerun")


 #   @st.cache_data
    def long_running_task():
        time.sleep(5) # Simulate a long-running task
        st.success("Task completed!")
        print("Loading...")
        st.write("Loading completed!")
    
    long_running_task()
    
 #   @st.cache_data    
    def load_uploaded_file(uploaded_file):
        return pd.read_csv(uploaded_file)
    
    
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:

        # Can be used wherever a "file-like" object is accepted:
        dataframe = load_uploaded_file(uploaded_file)
        st.write(dataframe)

    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    st.metric("Temperature", "70 °F", "1.2 °F")


##### MAINLAUNCH ##############

page = st.sidebar.selectbox('Select page',['Version Comparison','Period Comparison','Tests']) 
if page == 'Version Comparison':
    VersionComp()
elif page == 'Period Comparison':
    PeriodComp()
else:
    widgettest()