import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore!!!", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Martian SuperStore EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# File uploader
fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])

if fl is not None:
    filename = fl.name
    st.write(filename)
    # Check file extension and read accordingly
    if filename.endswith(('.csv', '.txt')):
        df = pd.read_csv(fl, encoding="ISO-8859-1")  # Use fl directly for uploaded files
    elif filename.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(fl)  # Use fl directly for Excel files
else:
    try:
        os.chdir(r"C:\Users\io\Documents\Peter\APP BUILDING\Martian store")
        df = pd.read_excel("Martianstore.xlsx")  # Read the Excel file Martianstore.xlsx
    except FileNotFoundError:
        st.error("Default file 'Martianstore.xlsx' not found in the directory. Please upload a file.")
        st.stop()

col1, col2 = st.columns((2))
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Getting the min and max date 
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

# We want to add sidebar
st.sidebar.header("Choose your filter: ")
# Create for Region
region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())
category = st.sidebar.multiselect("Pick your Category", df["Category"].unique())
