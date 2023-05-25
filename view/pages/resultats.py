import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Résultats", page_icon="📊")

# Colors definitions
primary_color = "#191970"
button_color = "#66CDAA"

# Apply the styles
st.markdown(
    f"""
    <style>
    .stButton > button {{
        background-color: {button_color};
        color: blue;
    }}
    .stButton button:focus,
    .stButton button:active {{
        background-color: {primary_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Mes résultats")

paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    ("Sélectionnez un thème", 'Métier', 'Animaux'))

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")