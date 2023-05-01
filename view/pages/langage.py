import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Langage", page_icon="🌍")

st.title("Langage")

langue = st.selectbox(
    'Veuillez choisir la langue que vous souhaitez apprendre :',
    ('Allemand', 'Anglais', 'Espagnol', 'Italien', 'Français', 'Mandarin', 'Néerlandais', 'Portugais'))

st.write('Vous avez séléctionner :', langue)

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")