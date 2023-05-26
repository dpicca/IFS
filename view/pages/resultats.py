import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import controler.controler as ctrl

st.set_page_config(page_title="Résultats", page_icon="📊")

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

st.title("Mes résultats")

cont=ctrl.Controller()

paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    (cont.show_all_packs_c())
)

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")