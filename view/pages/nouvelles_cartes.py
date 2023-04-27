import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Nouvelles cartes", page_icon="🃏")

st.title("Nouvelles cartes")

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")