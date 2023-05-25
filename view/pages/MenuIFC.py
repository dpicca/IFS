import streamlit as st
import time
import numpy as np
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

st.set_page_config(page_title="Menu IFC", page_icon="📄")

st.title("IFC ")

# Define custom colors
primary_color = "#191970"
button_color = "#FFB6C1"

# Apply styles
st.markdown(
    f"""
    <style>
    .stButton > button {{
        background-color: {button_color};
        color: white;
    }}
    .stButton button:focus,
    .stButton button:active {{
        background-color: {primary_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Create a grid of 2X2
# Show the menu bottoms in the grid
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

