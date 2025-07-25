import streamlit as st
from PIL import Image
import datetime

# ------------------ CONFIGURATION ------------------
st.set_page_config(page_title="AFRILAND IA", layout="wide")

USERS = {
    "user@afriland.cm": "password123",
    "admin@afriland.cm": "adminpass"
}

# ------------------ INITIALISATION ------------------
def init_session_state():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "email" not in st.session_state:
        st.session_state.email = ""
    if "history" not in st.session_state:
        st.session_state.history = []
    if "active_input" not in st.session_state:
        st.session_state.active_input = ""
    if "new_input" not in st.session_state:
        st.session_state.new_input = ""

init_session_state()

# ------------------ LOGO AFRILAND ------------------
@st.cache_resource
def get_logo():
    return Image.open("afriland_logo_1.png")

# ------------------ PAGE DE CONNEXION ------------------
def login_page():
    st.markdown("""
        <style>
            .centered {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: start;
                padding-top: 20px;
                text-align: center;
            }
            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 3px;
                padding: 3px 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.image(get_logo(), width=180)
    st.markdown("## CONNEXION IA - FIRST BANK")
    email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Connexion"):
        if email in USERS and USERS[email] == password:
            st.session_state.authenticated = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Email ou mot de passe incorrect.")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ PAGE PRINCIPALE ------------------
def main_page():
    # Sidebar
    with st.sidebar:
        st.image(get_logo(), width=120)
        st.markdown("### Historique")
        for idx, hist in enumerate(st.session_state.history[::-1]):
            if st.button(f"🕘 {hist[:25]}...", key=f"hist_{idx}"):
                st.session_state.active_input = hist
                st.rerun()

        st.markdown("---")
        with st.expander("👤 My Profile", expanded=False):
            st.markdown(f"**{st.session_state.email}**")
            if st.button("🔓 Déconnexion"):
                st.session_state.authenticated = False
                st.session_state.email = ""
                st.rerun()

    # Header avec bouton IA - AFRILAND cliquable
    st.markdown("""
        <style>
            .header-btn {
                background: none;
                border: none;
                font-size: 28px;
                color: red;
                font-weight: bold;
                cursor: pointer;
                padding: 10px 20px;
                margin-bottom: 10px;
                text-align: left;
            }
            .header-container {
                display: flex;
                justify-content: flex-start;
                align-items: center;
                border-bottom: 1px solid #ddd;
                background-color: #fff;
            }
        </style>
        <div class="header-container">
            <form action="" method="post">
                <button class="header-btn" name="reset_input">🤖 IA - AFRILAND</button>
            </form>
        </div>
    """, unsafe_allow_html=True)

    if st.query_params.get("reset_input") is not None:
        st.session_state.active_input = ""

    if st.session_state.active_input:
        st.info(f"**Dernière question :** {st.session_state.active_input}")

    # Zone de saisie type ChatGPT sans cadre ni fond gris
    st.markdown("""
        <style>
            .chat-input-wrapper {
                max-width: 900px;
                margin: 30px auto;
                display: flex;
                gap: 10px;
                align-items: stretch;
            }
            .chat-input-wrapper textarea {
                flex: 1;
                border: none;
                outline: none;
                resize: none;
                font-size: 16px;
                padding: 14px;
                border-radius: 8px;
                background-color: white;
                box-shadow: 0 0 0 1px #ccc;
            }
            .chat-input-wrapper button {
                background-color: red;
                color: white;
                border: none;
                padding: 14px 18px;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.form("form_input", clear_on_submit=True):
        st.markdown('<div class="chat-input-wrapper">', unsafe_allow_html=True)
        submitted = st.form_submit_button("➤")
        user_input = st.text_area("", value="", height=100, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        if submitted and user_input.strip():
            st.session_state.active_input = user_input.strip()
            st.session_state.history.append(user_input.strip())
            st.rerun()

# ------------------ LANCEMENT ------------------
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
