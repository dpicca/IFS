import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import controler.controler as ctrl
import matplotlib.pyplot as plt


st.set_page_config(page_title="Résultats", page_icon="📊")

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

st.title("Mes résultats")

# Import the Controller() class
cont = ctrl.Controller()

# Select a pack
paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    (cont.show_all_packs_c())
)

# Graphic
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [6, 7, 6, 9, 8, 4, 5, 8, 10, 8]

# Create the graphic
plt.plot(x, y, label='Résultats', linewidth=2)
plt.xlabel('Séries')
plt.ylabel('Réponses')
plt.title('Progression des résultats')
plt.legend()

# Scales
plt.xlim(1, 10)
plt.ylim(1, 10)

# Show the graphic
st.pyplot(plt)

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")