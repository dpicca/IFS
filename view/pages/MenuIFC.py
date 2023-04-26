import streamlit as st
import time
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Menu IFC", page_icon="📈")

st.markdown("# IFC ")

buttonMesCartes = st.button("Mes cartes")
if buttonMesCartes:
    switch_page("mes_cartes")

buttonNouvellesCartes = st.button("Nouvelles cartes")
if buttonNouvellesCartes:
    switch_page("nouvelles_cartes")

buttonResultats = st.button("Mes résultats")
if buttonResultats:
    switch_page("resultats")

buttonLangage = st.button("Langage")
if buttonLangage:
    switch_page("langage")

buttonAPropos = st.button("À propos")
if buttonAPropos:
    switch_page("a_propos")

buttonSeDeco = st.button("Se déconnecter")
if buttonSeDeco:
    switch_page("user_login")
