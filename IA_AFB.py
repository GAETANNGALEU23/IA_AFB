import streamlit as st
from PIL import Image
import datetime


def login_page():
    st.markdown("""
        <style>
            .login-overlay {
                position: fixed;
                top: 0; left: 0;
                width: 100%; height: 100%;
                background-color: rgba(0, 0, 0, 0.3);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
            }

            .login-box {
                background-color: white;
                padding: 40px 30px;
                border-radius: 12px;
                box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
                width: 100%;
                max-width: 400px;
                text-align: center;
            }

            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 30px;
                margin-top: 15px;
            }

            input, .stTextInput input {
                text-align: center;
            }
        </style>

        <div class="login-overlay">
            <div class="login-box">
    """, unsafe_allow_html=True)

    st.image(get_logo(), width=100)
    st.markdown("## CONNEXION IA")

    email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm", label_visibility="visible")
    password = st.text_input("Mot de passe", type="password", label_visibility="visible")

    if st.button("Connexion"):
        if email in USERS and USERS[email] == password:
            st.session_state.authenticated = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Email ou mot de passe incorrect.")

    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)
