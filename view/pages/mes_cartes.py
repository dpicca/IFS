import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

st.title("Mes cartes")

# Sélectionner un thème de cartes
paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    ("Sélectionnez un thème", 'Métier', 'Animaux')
)

if paquet != "Sélectionnez un thème":
    st.write('Vous avez sélectionné :', paquet)

    # Afficher l'expander uniquement si quelque chose est sélectionné
    with st.expander("Recto de la carte"):
        st.write("Verso de la carte")
        buttonJuste = st.button("Vrai")
        buttonFaux = st.button("Faux")


buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")

