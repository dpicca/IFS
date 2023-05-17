import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page
from controler import controler
#commentaire

cartes = controler.Controller()

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

st.title("Mes cartes")

paquet = st.selectbox(
    'Sélectionnez un paquet :',
    (
        cartes.show_data_controler("métiers_anglais")
    )
)

st.write('Vous avez sélectionné :', paquet)

with st.expander("Recto de la carte"):
    st.write("Verso de la carte")


buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")

