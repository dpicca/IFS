"""
This file creates a simple and interactive user interface, providing easy navigation between different features.
The code utilizes interactive buttons to enable users to select different menu options.
When a button is clicked, the corresponding page is activated using the switch_page() function.
The code also applies custom styles to the buttons, defining specific background and text colors.
"""
import streamlit as st
import time
import numpy as np
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# Configure Streamlit page
st.set_page_config(page_title="Menu IFC", page_icon="📄")

# Title of the application
st.title("IFC ")

# Define custom colors
primary_color = "#FFFFF"
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
    # "My Cards" button
    if st.button("Mes cartes"):
        switch_page("mes_cartes")

    # "New Cards" button
    if st.button("Nouvelles cartes"):
        switch_page("nouveau_paquet")

with col2:
    # "My Results" button
    if st.button("Mes résultats"):
        switch_page("resultats")

    # "Log Out" button
    if st.button("Se déconnecter"):
        switch_page("user_login")

