"""
This main file handles user authentication, including login, registration,
password reset, and user details update.
"""

import streamlit as st # for creating the application
import streamlit_authenticator as stauth # for managing user authentication
import yaml # for reading and writing YAML configuration files
from yaml.loader import SafeLoader
from streamlit_extras.switch_page_button import switch_page # for handling page switching in the application

# open yaml file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# define update user function
def update_config():
    """
    Updates the configuration file with the current configuration.
    This function writes the 'config' dictionary to the 'config.yaml' file.
    """
    # Saving config file
    with open('./config.yaml', 'w') as file:
        yaml.dump(config, file)


# Creating an instance of the Authenticate class
authenticator = stauth.Authenticate(
    config['credentials'],             # User credentials
    config['cookie']['name'],          # Name of the authentication cookie
    config['cookie']['key'],           # Key of the authentication cookie
    config['cookie']['expiry_days'],   # Expiration days of the authentication cookie
    config['preauthorized']            # Preauthorized users
)


# Creating login widget
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    # If authentication is successful, display welcome message and homepage button
    authenticator.logout('Logout', 'main') # Logout button
    st.title(f'Welcome *{name}*')
    # Homepage button to switch to the home page
    homepagebutton = st.button("Ma page d'accueil")
    if homepagebutton:
        switch_page("MenuIFC")
    st.header('À propos') # About section
    st.markdown(
        "Intelligent FlashCards est un logiciel permettant d’apprendre de nouvelles langues facilement tout en observant sa progression.\n"
        "L’utilisation de cartes d’apprentissage personnalisables et l’aide de l’intelligence artificielle permettant de générer des cartes automatiquement autour d’un thème donné proposent à l’utilisateur une nouvelle manière ludique de se familiariser avec des langues inconnues.\n"
        "IFC s’adapte à tous les niveaux d’apprentissage de langues.\n"
        "De plus, l’onglet “mes résultats” permet à l’utilisateur de visulaiser sa progression.\n"
        "Logiciel créé par le groupe LOLS, 2023.")

elif authentication_status is None:
    # If authentication status is None, it means a new user needs to register
    try:
        # Register a new user
        if authenticator.register_user('Register user', preauthorization=False):
            update_config()
            st.success('User registered successfully')

    except Exception as e:
        st.error(e)
    st.warning('Please enter your username and password')
elif authentication_status is False:
    # If authentication status is False, the user failed to login
    try:
        # Creating a forgot password widget
        username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
        if username_forgot_pw:
            st.success('New password sent securely')
            # Random password to be transferred to user securely
        else:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

    try:
        # Creating a forgot username widget
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
        # If authentication is successful, allow the user to reset their password
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
        update_config() # Update the configuration file with the modified details
    except Exception as e:
        st.error(e)
