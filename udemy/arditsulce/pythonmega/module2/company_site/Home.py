import streamlit as st
import pandas as pd

st.set_page_config(page_title="Best Company", page_icon="🚀", layout="wide", initial_sidebar_state="auto")

st.write("# Welcome to Best Company! 🚀")

st.write("## Our Mission")
st.write("Our mission is to provide the best services to our customers. We believe in quality and customer satisfaction. We are here to help you with all your needs.")
st.write("## Our Vision")
st.write("Our vision is to become the best company in the world. We aim to provide the best products and services to our customers. We are committed to excellence and innovation.")

st.write("---")

st.write("## Our Team")

column1, column2, column3 = st.columns(3)

df = pd.read_csv("data.csv", sep=",")

with column1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.image("images/" + row["image"], width=300)
        st.subheader(row["role"])
        st.write("---")

with column2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.image("images/" + row["image"], width=300)
        st.subheader(row["role"])
        st.write("---")

with column3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.image("images/" + row["image"], width=300)
        st.subheader(row["role"])
        st.write("---")