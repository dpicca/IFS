import streamlit as st
# import pandas as pd
# import pydeck as pdk
# from urllib.error import URLError
from streamlit_extras.switch_page_button import switch_page
import controler.controler as ctrl

st.set_page_config(page_title="Mes cartes", page_icon="🃏")

st.title("Mes cartes")
cont=ctrl.Controller()
# Select a theme from a dropdown

paquet = st.selectbox(
    'Sélectionnez un thème de cartes :',
    (cont.show_all_packs_c())
)

# Show the expender only if something is chosen
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


buttonRetourMenu = st.button("Retour au menu")
if buttonRetourMenu:
    switch_page("MenuIFC")
