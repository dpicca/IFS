import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page

# open yaml file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# define update user function
def update_config():
    # Saving config file
    with open('./config.yaml', 'w') as file:
        yaml.dump(config, file)


# Creating authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


# creating login widget
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.title(f'Welcome *{name}*')
    homepagebutton = st.button("Ma page d'accueil")
    if homepagebutton:
        switch_page("MenuIFC")
    st.header('À propos')
    st.markdown(
        "Intelligent FlashCards est un logiciel permettant d’apprendre de nouvelles langues facilement tout en observant sa progression.\n"
        "L’utilisation de cartes d’apprentissage personnalisables et l’aide de l’intelligence artificielle permettant de générer des cartes automatiquement autour d’un thème donné proposent à l’utilisateur une nouvelle manière ludique de se familiariser avec des langues inconnues.\n"
        "IFC s’adapte à tous les niveaux d’apprentissage de langues.\n"
        "De plus, l’onglet “mes résultats” permet à l’utilisateur de visulaiser sa progression.\n"
        "Logiciel créé par le groupe LOLS, 2023.")

elif authentication_status is None:
    # Creating a new user registration widget
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            update_config()
            st.success('User registered successfully')

    except Exception as e:
        st.error(e)
    st.warning('Please enter your username and password')
elif authentication_status is False:

    # Creating a forgot password widget
    try:
        username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
        if username_forgot_pw:
            st.success('New password sent securely')
            # Random password to be transferred to user securely
        else:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

    # Creating a forgot username widget
    try:
        username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
        if username_forgot_username:
            st.success('Username sent securely')
            # Username to be transferred to user securely
        else:
            st.error('Email not found')
    except Exception as e:
        st.error(e)

    st.error('Username/password is incorrect')



# Update user details widget
if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
        update_config()
    except Exception as e:
        st.error(e)
