import streamlit as st
import plotly.express as px
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Setting the Page
st.set_page_config(page_title="Martian_Store_Dashboard!!!", page_icon=":bar_chart:", layout="wide")

# Setting the title of the page and aligning the title up on the page
st.title(" :bar_chart: Martian Store EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# File Uploader
fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])

# File handling logic using if
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename)
else:
    os.chdir(r"C:\Users\io\Documents\Peter\APP BUILDING\Martian store")
    df = pd.read_xlsx("Martianstore")
