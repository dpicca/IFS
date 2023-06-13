"""
This file uses the Streamlit library to display results.
It also uses Matplotlib to generate a graph representing the progression of the results.
"""

import streamlit as st # the main library for creating web applications
from streamlit_extras.switch_page_button import switch_page # a module for adding a page navigation button
import controler.controler as ctrl # a module containing the Controller class for interacting with data
import matplotlib.pyplot as plt # a library for creating plots

# Configuring the Streamlit page:
# Setting the page title using page_title.
# Setting the page icon using page_icon.
st.set_page_config(page_title="Résultats", page_icon="📊")


# Define custom colors
primary_color = "#FFFFF"
button_color = "#FFB6C1"

# Apply custom styles
st.markdown( # function of Streamlit to apply custom CSS styles to buttons
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

# Selecting a pack:
# Using st.selectbox to display a dropdown list of available packs.
# Calling the show_all_packs_c method of the Controller instance cont to retrieve the packs.
paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    (cont.show_all_packs_c())
)

# Graphic
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [6, 7, 6, 9, 8, 4, 5, 8, 10, 8]

# Create the graphic
plt.plot(x, y, label='Résultats', linewidth=2) # to plot the graph curve.
plt.xlabel('Séries')
plt.ylabel('Réponses')
plt.title('Progression des résultats')
plt.legend() # Displaying the graph legend

# Setting the axis scales
plt.xlim(1, 10)
plt.ylim(1, 10)

# Show the graphic
st.pyplot(plt)

# Adding a "Return to Menu" button using st.button.
# When the button is clicked, the switch_page function is called to navigate to the "MenuIFC" page.
buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")