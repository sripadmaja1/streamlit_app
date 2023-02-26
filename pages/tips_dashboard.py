import streamlit as st
import pandas as pd
import os
from matplotlib import image
import plotly.express as px

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "tips.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

st.title("Dashboard - TIPS")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

time=st.selectbox('time :',df['time'].unique())
col1,col2=st.columns(2)

fig_1=px.histogram(df[df["time"]==time],x='day',labels={'value':'day'},title='count of customers w.r.t time and day')
col1.plotly_chart(fig_1,use_container_width=True)

fig_2= px.bar(df[df["time"]==time],x="smoker",labels={'count':'count of customers'},height=500,title='count of customers who smoke')
col2.plotly_chart(fig_2,use_container_width=True)

fig_3=px.box(df,x="sex",y="total_bill",color='time',title='gender wise bill w.r.t time')
col1.plotly_chart(fig_3,use_container_width=False)