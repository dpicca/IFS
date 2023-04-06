import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


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
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status is None:
    st.warning('Please enter your username and password')
elif authentication_status is False:
    st.error('Username/password is incorrect')

# creating password reset widget
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

# Creating a new user registration widget
try:
    if authenticator.register_user('Register user', preauthorization=False):
        update_config()
        st.success('User registered successfully')

except Exception as e:
    st.error(e)

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

# Update user details widget
if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
        update_config()
    except Exception as e:
        st.error(e)
