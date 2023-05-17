import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Nouveau paquet", page_icon="🃏")

st.title("Nouveau paquet")

# Nouveau paquet
new_paquet = st.text_input("Choisir le nom du paquet :")
buttonCreate = st.button("Créer")

if buttonCreate:
    # Nouvelle carte
    new_word = st.text_input("Nouveau mot :")
    new_translation = st.text_input("Traduction :")

    # Mettre les boutons l'un à côté de l'autre
    col1, col2 = st.columns(2)
    with col1:
        st.button("Nouvelle carte")
    with col2:
        st.button("Valider")

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")
