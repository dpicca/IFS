import streamlit as st
# import pandas as pd
# import pydeck as pdk
# from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page
import controler.controler as ctrl

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

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

st.title("Mes cartes")
cont=ctrl.Controller()
# Select a theme from a dropdown

paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    (cont.show_all_packs_c())
)

question_list = [question for question in list(cont.show_question_c("métiers_anglais"))]

# Fonction qui génère une dictionnaire ECRASE LES REPONSES
# def retrieve_cards(dict):
#     question_tuples = cont.show_question_c("métiers_anglais")
#     print(question_tuples)
#     for item in cont.show_question_c("métiers_anglais"):
#         question = str(item)
#         dict[question] = "answer"
#     for item in cont.show_answer_c("métiers_anglais"):
#         answer = str(item)
#         dict[question_list[len(question_list)-1]] = answer
#     return dict

# Test avec un dictionnaire QUI MARCHE
# if paquet != "Sélectionnez un thème":
#     st.write('Vous avez sélectionné :', paquet)
#     cards_paquet = dict()
#     retrieve_cards(cards_paquet)
#     for question, answer in cards_paquet.items():
#         with st.expander(question):
#             st.write(answer)
            # buttonJuste = st.button("Vrai")
            # buttonFaux = st.button("Faux")

# Test question + answer en double
if paquet != "Sélectionnez un thème":
    st.write('Vous avez sélectionné :', paquet)
    for item in cont.show_question_c("métiers_anglais"):
        question = str(item)
        for item in cont.show_answer_c("métiers_anglais"):
            answer = str(item)
            with st.expander(question):
                st.write(answer)
            #buttonJuste = st.button("Vrai")
            #buttonFaux = st.button("Faux")

# Show the expander only if something is chosen
# Test question OK
if paquet != "Sélectionnez un thème":
    st.write('Vous avez sélectionné :', paquet)
    for item in cont.show_question_c("métiers_anglais"):
        question = str(item)
        # for answers_item in cont.show_answer_c("métiers_anglais"):
        #     answer = str(answers_item)
        with st.expander(question):
            st.write("answer")
            #buttonJuste = st.button("Vrai")
            #buttonFaux = st.button("Faux")

# Test answer OK
if paquet != "Sélectionnez un thème":
    st.write('Vous avez sélectionné :', paquet)
    for item in cont.show_answer_c("métiers_anglais"):
        answer = str(item)
        # for answers_item in cont.show_answer_c("métiers_anglais"):
        #     answer = str(answers_item)
        with st.expander(answer):
            st.write("answer")
            #buttonJuste = st.button("Vrai")
            #buttonFaux = st.button("Faux")


buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")

