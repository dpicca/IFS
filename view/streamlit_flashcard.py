#Creation du login

import streamlit as st

# Créer une liste pour stocker les utilisateurs enregistrés
users = []

# Créer une classe User pour stocker les informations de l'utilisateur
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Définir l'en-tête de la page
st.title("Page de connexion / Inscription")

# Créer une variable pour stocker l'état de l'utilisateur (connecté / non connecté)
state = st.session_state.get("state", {"logged_in": False})

# Créer les champs de saisie pour l'identifiant et le mot de passe
username = st.text_input("Nom d'utilisateur")
password = st.text_input("Mot de passe", type="password")

# Ajouter un bouton pour soumettre les informations de connexion
if st.button("Se connecter"):
    # Vérifier si l'utilisateur est enregistré
    for user in users:
        if user.username == username and user.password == password:
            state["logged_in"] = True
            st.success("Connecté avec succès!")
            break
    else:
        st.error("Identifiant ou mot de passe incorrect.")

# Ajouter un bouton pour s'inscrire
if st.button("S'inscrire"):
    # Vérifier si l'utilisateur n'est pas déjà enregistré
    if any(user.username == username for user in users):
        st.error("Nom d'utilisateur déjà pris.")
    else:
        # Ajouter l'utilisateur à la liste
        users.append(User(username, password))
        st.success("Inscription réussie!")

# Afficher le contenu de la page en fonction de l'état de l'utilisateur
if state["logged_in"]:
    st.write("Contenu de la page pour les utilisateurs connectés.")
else:
    st.write("Contenu de la page pour les utilisateurs non connectés.")
