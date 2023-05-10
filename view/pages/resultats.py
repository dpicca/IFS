import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Résultats", page_icon="📊")

st.title("Mes résultats")

title = st.text_input('Titre :')
language = st.text_input('Langue :')

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")