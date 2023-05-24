import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page
import model.sqlite_flashcard as Models

def show_all_packs_v(list):
    for item in list:
        paquet.append(item)

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

st.title("Mes cartes")

# Select a theme from a dropdown
paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    ()
)

if paquet != "Sélectionnez un thème":
    st.write('Vous avez sélectionné :', paquet)

    # Show the expender only if something is chosen
    with st.expander("Recto de la carte"):
        st.write("Verso de la carte")
        buttonJuste = st.button("Vrai")
        buttonFaux = st.button("Faux")


buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")
