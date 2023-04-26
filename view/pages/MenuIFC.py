import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Menu IFC", page_icon="📈")

st.markdown("# IFC ")

buttonMesCartes = st.button("Mes cartes")
buttonNouvellesCartes = st.button("Nouvelles cartes")
buttonResultats = st.button("Mes résultats")
buttonLangage = st.button("Langage")
buttonAPropos = st.button("À propos")
buttonSeDeco = st.button("Se déconnecter")
