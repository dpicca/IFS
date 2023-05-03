import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

st.title("Mes cartes")

title = st.text_input('Titre :')
language = st.text_input('Langue :')

st.markdown('Veuillez séléctionner un paquet de cartes :')

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")
