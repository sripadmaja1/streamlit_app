import streamlit as st
import os


st.header(' :blue[Hello everyone]! :wave: ')

st.title('welcome to my page')

st.subheader('**_About me :_**')
def jls_extract_def():
    return '''    I am Padmaja,
    i have completed my btech in computer science and engineering in 2022. 
    Now, i am currently enrolled in Data Science course and 
    recently joined this internship.'''


st.text(jls_extract_def())
st.write('follow me on my LinkedIn')

if st.button('LinkedIn'):

    st.write('www.linkedin.com/in/k-sri-padmaja')




