import streamlit as st
import time
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Menu IFC", page_icon="📄")

st.title("IFC ")

# Créer une grille de 2x2 boutons
col1, col2 = st.columns(2)

with col1:
    if st.button("Mes cartes"):
        switch_page("mes_cartes")

    if st.button("Nouvelles cartes"):
        switch_page("nouveau_paquet")

with col2:
    if st.button("Mes résultats"):
        switch_page("resultats")

    if st.button("Se déconnecter"):
        switch_page("user_login")

