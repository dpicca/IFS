import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page
from controler import controler


controler = controler.Controller()

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

st.title("Mes cartes")

# Select a theme from a dropdown
paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    (controler.show_all_packs_c())
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

