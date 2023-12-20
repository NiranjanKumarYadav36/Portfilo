import pandas
import streamlit as st


st.set_page_config(layout='wide')

col1, col2 = st.columns(2, gap='small')

with col1:
    st.image("images/photo1.jpg")


with col2:
    st.title("Niranjan Kumar Yadav")
    content = """ 
    Hi, I am Niranjan.\n
    Currently I am an engineering student studying at Don Bosco Institute of Technology - Mumbai, India.
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Pyton. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2, gap='large')


df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, rows in df[:10].iterrows():
        st.header(rows['title'])
        st.write(rows['description'])
        st.image("images/" + rows['image'])
        st.write(f"[Source Code]({rows['url']})")

with col4:
    for index, rows in df[10:].iterrows():
        st.header(rows['title'])
        st.write(rows['description'])
        st.image("images/" + rows['image'])
        st.write(f"[Source Code]({rows['url']})")
