import streamlit as st
# import pandas as pd
# import pydeck as pdk
# from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page
import controler.controler as ctrl

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

# Define custom colors
primary_color = "#191970"
button_color = "#FFB6C1"

# Apply styles
st.markdown(
    f"""
    <style>
    .stButton > button {{
        background-color: {button_color};
        color: white;
    }}
    .stButton button:focus,
    .stButton button:active {{
        background-color: {primary_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Mes cartes")
cont=ctrl.Controller()
# Select a theme from a dropdown

paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    (cont.show_all_packs_c())
)

if paquet != "Sélectionnez un thème":
    st.write('Vous avez sélectionné :', paquet)
    questions = cont.show_question_c("métiers_anglais")
    answers = cont.show_answer_c("métiers_anglais")
    for i, (question, answer) in enumerate(zip(questions, answers)):
        question_str = str(question)
        answer_str = str(answer)
        with st.expander(question_str):
            st.write(answer_str)
            st.button("Juste", key=f"Juste_{i}")
            st.button("Faux", key=f"Faux_{i}")


buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")

