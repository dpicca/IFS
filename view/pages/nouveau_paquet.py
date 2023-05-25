import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Nouveau paquet", page_icon="🃏")

# Colors definitions
primary_color = "#191970"
button_color = "#66CDAA"

# Apply the styles
st.markdown(
    f"""
    <style>
    .stButton > button {{
        background-color: {button_color};
        color: blue;
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

# New pack
new_paquet = st.text_input("Choisir le nom du paquet :")
buttonCreate = st.button("Créer")

if buttonCreate and new_paquet:
    # Step 2: Creating new cards
    st.write("Création de nouvelles cartes :")
    new_words = []
    new_translations = []
    add_new_card = True

    while add_new_card:
        with st.form("new_card_form"):
            new_word = st.text_input("Nouveau mot :", key="new_word")
            new_translation = st.text_input("Traduction :", key="new_translation")
            submitted = st.form_submit_button("Ajouter")

            if submitted:
                if new_word and new_translation:
                    new_words.append(new_word)
                    new_translations.append(new_translation)
                    st.success("Nouvelle carte créée avec succès !")
                    st.write(f"Mot : {new_word}, Traduction : {new_translation}")
                else:
                    st.warning("Veuillez entrer le nouveau mot et sa traduction.")

        add_new_card = submitted  # Set add_new_card to False if "Ajouter" button is not clicked

    # Step 4: Validation
    if st.button("Valider"):
        # Process the new words and translations here (e.g., save them to a database or data structure)
        for word, translation in zip(new_words, new_translations):
            st.write(f"Mot : {word}, Traduction : {translation}")
        st.success("Cartes créées avec succès !")
        # new_paquet.empty() CA NE MARCHE PAS !!!!!
elif buttonCreate and not new_paquet:
    st.warning("Veuillez entrer le nom du paquet.")

buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")
