import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

st.title("Mes cartes")

option = st.selectbox(
    'Sélectionnez un thème de cartes :',
    ('Thème 1', 'Thème 2', 'Thème 3'))

st.write('Vous avez sélectionné :', option)

with st.container():
   st.write("This is inside the container")
st.write("This is outside the container")



buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")

