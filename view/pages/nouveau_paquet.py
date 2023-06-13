"""
This file allows the application to create new flashcards.
Users can input a packet name, add new words and their translations
and validate the creation of the flashcards. The code includes a section
to define custom colors. You can modify the variables primary_color
and button_color to change the appearance of buttons in the application.
The code also includes a button to return to the menu.
"""

import streamlit as st
from streamlit_extras.switch_page_button import switch_page # to switch between different pages
import controler.controler as ctrl

st.set_page_config(page_title="Nouveau paquet", page_icon="🃏")

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

st.title("Nouveau paquet")

# Import class Controller()
cont = ctrl.Controller()

# Function to submit form
def submit_form(question, answer, paquet):
    """
   Submits the form by adding the question and answer to the specified packet.

    Args:
        question (str): The content of the question.
        answer (str): The content of the answer.
        paquet (str): The name of the packet.

    Returns:
        tuple: The result of adding the question and answer.

    """
    submit_question = cont.add_question_c(question, paquet)
    submit_answer = cont.add_answer_c(answer, paquet)
    return submit_question, submit_answer

# New pack
new_paquet = st.text_input("Choisir le nom du paquet :")
buttonCreate = st.button("Créer")


# Open the form for the new cards
if buttonCreate and new_paquet:
    # Step 2: Creating new cards
    st.write("Création de nouvelles cartes :")
    # to store the new words and their translations :
    new_words = list()
    new_translations = list()
    # is initialized to True to enter the while loop :
    add_new_card = True

    while add_new_card:
        with st.form("new_card_form"):
            # displays a text input field for the new item to be added (word) :
            new_word = st.text_input("Nouveau mot :", key="new_word")
            # displays a text input field for the corresponding translation :
            new_translation = st.text_input("Traduction :", key="new_translation")
            # displays an "Add" button to submit the form :
            submitted = st.form_submit_button("Ajouter")

            # If the user clicks the "Add" button (submitted is True), the code checks
            # if the word and translation input fields are not empty.
            if submitted:
                # If the input fields are not empty, the word and translation are added :
                if new_word and new_translation:
                    new_words.append(new_word)
                    new_translations.append(new_translation)
                    st.success("Nouvelle carte créée avec succès !")
                    # The values of the word and translation are also displayed,
                    # using st.write() to show them to the user :
                    st.write(f"Mot : {new_word}, Traduction : {new_translation}")
                else:
                    # If the input fields are empty, a warning is displayed,
                    # asking the user to enter the new word and its translation:
                    st.warning("Veuillez entrer le nouveau mot et sa traduction.")

        # set to False if the "Add" button is not clicked, which will exit the while loop :
        add_new_card = submitted  # Set add_new_card to False if "Ajouter" button is not clicked

    # Step 4: Validation
    if st.button("Valider"):
        # Process the new words and translations here (e.g., save them to a database or data structure)
        for word, translation in zip(new_words, new_translations):
            submit_form(word, translation, new_paquet)
            st.write(f"Mot : {word}, Traduction : {translation}")
        st.success("Cartes créées avec succès !")
        # new_paquet.empty() CA NE MARCHE PAS !!!!!
elif buttonCreate and not new_paquet:
    st.warning("Veuillez entrer le nom du paquet.")

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC") # to switch to the "MenuIFC" page
