import streamlit as st
from PIL import Image

# ------------------ CONFIGURATION ------------------
st.set_page_config(page_title="AFRILAND IA", layout="wide")

USERS = {
    "user@afriland.cm": "password123",
    "admin@afriland.cm": "adminpass"
}

def init_session_state():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "email" not in st.session_state:
        st.session_state.email = ""

init_session_state()

def login_page():
    st.markdown("""
        <style>
            /* Cache sidebar/header/footer */
            header, footer, .stSidebar {
                display: none;
            }

            /* Fond sombre */
            .overlay {
                position: fixed;
                top: 0; left: 0;
                width: 100vw; height: 100vh;
                background-color: rgba(0,0,0,0.6);
                z-index: 9998;
            }

            /* Conteneur central */
            .login-box {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 0 25px rgba(0, 0, 0, 0.3);
                z-index: 9999;
                width: 90%;
                max-width: 350px;
                text-align: center;
            }

            .login-box h2 {
                color: red;
                font-size: 22px;
                margin-bottom: 20px;
            }

            .stTextInput > div > input {
                font-size: 14px;
                padding: 8px;
            }

            .stButton button {
                width: 100%;
                padding: 8px;
                font-size: 14px;
                font-weight: bold;
                background-color: red;
                color: white;
                border-radius: 8px;
            }
        </style>

        <div class="overlay"></div>
        <div class="login-box">
    """, unsafe_allow_html=True)

    st.image("afriland_logo_1.png", width=80)  # Assure-toi que ce fichier existe
    st.markdown("## Connexion AFRILAND IA")

    email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Connexion"):
        if email in USERS and USERS[email] == password:
            st.session_state.authenticated = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Email ou mot de passe incorrect.")

    st.markdown("</div>", unsafe_allow_html=True)

def main_page():
    st.success(f"Bienvenue {st.session_state.email} ! 🎉")

if not st.session_state.authenticated:
    login_page()
else:
    main_page()
