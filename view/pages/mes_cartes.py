"""
In this file, the Streamlit application displays a page titled
"Mes cartes" with a theme selection dropdown and a list of questions and answers.
Each question is displayed in an expander, and buttons are provided for the user to respond (Juste or Faux).
The selected response is captured and processed by the Controller instance.
The code also applies custom CSS styling to the buttons, sets the page configuration,
and provides a button to return to the menu page using the switch_page function.
"""
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import controler.controler as ctrl

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

# Set page configuration and styling
primary_color = "#FFFFF"
button_color = "#FFB6C1"

# Apply custom CSS styling to buttons
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

# Display the title of the page
st.title("Mes cartes")

# Import the Controller() class
cont=ctrl.Controller()

# Select a theme from a dropdown
paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    (cont.show_all_packs_c())
)

# If a pack is selected show the cards
if paquet != "Sélectionnez un thème":
    st.write('Vous avez sélectionné :', paquet)
    questions = cont.show_question_c("métiers_anglais")
    answers = cont.show_answer_c("métiers_anglais")
    # Iterate over each question and answer pair
    for i, (question, answer) in enumerate(zip(questions, answers)):
        question_str = str(question)
        answer_str = str(answer)
        with st.expander(question_str):
            st.write(answer_str)
            # Add buttons for user response (Juste or Faux)
            if st.button("Juste", key=f"Juste_{i}"):
                st.warning("C'est juste !", icon= "🥳")
                #cont.answeruser_add_data_c(12, 13, 1)
            if st.button("Faux", key=f"Faux_{i}"):
                st.warning("C'est faux…", icon="❌")
                #cont.answeruser_add_data_c(12, 13, 0)


# Add a button to return to the menu page
buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")

