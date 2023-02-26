import streamlit as st
from matplotlib import image
import pandas as pd
import os
import plotly.express as px

st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)
df=pd.read_csv(DATA_PATH)
df=df.dropna()
st.dataframe(df)

gender = st.selectbox("gender: ", df["sex"].unique())
clas=st.selectbox("embark_town:",df['embark_town'].unique())
col1,col2=st.columns(2)

fig_1= px.pie(df[df["sex"]==gender],names="survived", title="Gender wise survived Percentage ")
col1.plotly_chart(fig_1,use_container_width=True)

fig_2=px.histogram(df[df["embark_town"]== clas ],x='survived',title='survival count w.r.t embark_twon')
col2.plotly_chart(fig_2,use_container_width=True)

fig_3=px.box(x=df["pclass"],y=df["age"],labels={'x':'pclass','y':'age'},title="people's age w.r.t pclass")
col1.plotly_chart(fig_3,use_container_width=False)
