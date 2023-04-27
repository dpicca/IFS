import streamlit as st
import time
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="À propos", page_icon="❓")

st.title("À propos ")

st.markdown("Intelligent FlashCards est un logiciel permettant d’apprendre de nouvelles langues facilement tout en observant sa progression.\n"
            "L’utilisation de cartes d’apprentissage personnalisables et l’aide de l’intelligence artificielle permettant de générer des cartes automatiquement autour d’un thème donné proposent à l’utilisateur une nouvelle manière ludique de se familiariser avec des langues inconnues.\n"
            "IFC s’adapte à tous les niveaux d’apprentissage de langues.\n"
            "De plus, l’onglet “mes résultats” permet à l’utilisateur de visulaiser sa progression.\n"
            "Logiciel créé par le groupe LOLS, 2023.")

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")