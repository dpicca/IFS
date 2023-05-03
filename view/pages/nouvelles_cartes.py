import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Nouvelles cartes", page_icon="🃏")

st.title("Nouvelles cartes")

new_cards = st.text_input('Veuillez choisir la langue dans laquelle vous souhaiteriez traduire vos cartes :')

st.markdown('Veuillez choisir le moyen de créer vos cartes :')
manually = st.checkbox('Manuellement')
automatically = st.checkbox('Automatiquement')

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")