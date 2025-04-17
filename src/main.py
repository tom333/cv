
import streamlit as st
from content import cv
from crew import CvCrew
import streamlit.components.v1 as components

from dotenv import load_dotenv

load_dotenv()

st.title("Thomas Guyader")
st.header("Architecte Data")

if "cv" not in st.session_state:
    st.session_state["cv"] = cv
show_cv = st.markdown(st.session_state["cv"])

st.sidebar.title("Profil recherché")
profile = st.sidebar.text_area("Profil recherché", placeholder="Mettre ici la description du poste à pourvoir", height=200, label_visibility="hidden")


def generate_cv():
    with st.spinner("Wait for it...", show_time=True):
        inputs = {
            'profile': profile,
            'github_url': 'https://github.com/tom333, https://github.com/tguyader',
        }

        try:
            st.session_state["cv"] = CvCrew().crew().kickoff(inputs=inputs)
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e}")


st.sidebar.button("Générer le nouveau CV", on_click=generate_cv)
