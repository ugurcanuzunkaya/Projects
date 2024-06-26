import streamlit as st
import pandas as pd

st.set_page_config(page_title="Uğurcan Uzunkaya", page_icon="🚀", layout="wide", initial_sidebar_state="auto")

column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.png", width=500)

with column2:
    st.title("Welcome to my portfolio! 🚀")
    content = """
    👋🏽 Hi, I'm Uğurcan Uzunkaya, a passionate Software Engineer specializing in 3D and 2D modeling systems. Currently, I work at Eleport Cloud Services, where I enhance user experiences through innovative 3D modeling. With a strong background in Industrial Engineering from Eskisehir Technical University, I aim to leverage artificial intelligence to help businesses make better decisions.

    📚 I've conducted extensive research on green energy and optimization, reflected in my thesis on tiny houses and sustainable living. My future goals include becoming a Senior Data Scientist at Nvidia or Google and founding a startup focused on AI, cloud computing, and green energy.

    💻 I have hands-on experience with various technologies, including Python, AWS, Django, Docker, TensorFlow, and Keras. My projects range from NLP systems for process mining to predictive maintenance and factory production simulations.

    🌇 Outside of work, I enjoy exploring art, nature, and personal development. I'm committed to continuous learning and mentoring others in their tech journeys.

    📬 Feel free to reach out for collaboration or inquiries! 😄


    """
    st.info(content)


st.write("---")
st.write("## Projects")
st.write("Here are some of my projects:")


column3, column4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with column3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code for {row['title']}]({row['url']})")
        st.write("---")


with column4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code for {row['title']}]({row['url']})")
        st.write("---")


