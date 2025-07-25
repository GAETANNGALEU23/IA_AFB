import streamlit as st
from PIL import Image

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
                padding-top: 40px;
                text-align: center;
            }
            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 3px;
                padding: 6px 12px;
            }
            .element-container:has(input) input {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
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
    # --------------- SIDEBAR -----------------
    with st.sidebar:
        st.image(get_logo(), width=120)
        st.markdown("### Historique")
        for idx, hist in enumerate(st.session_state.history[::-1]):
            if st.button(f"🕘 {hist[:25]}...", key=f"hist_{idx}"):
                st.session_state.active_input = hist
                st.rerun()
        
        st.markdown("---")

        with st.expander("👤 Mon Profil", expanded=False):
            st.markdown(f"**{st.session_state.email}**")
            if st.button("🔓 Déconnexion"):
                st.session_state.authenticated = False
                st.session_state.email = ""
                st.rerun()

    # --------------- TÊTE DE PAGE -----------------
    col1, col2 = st.columns([1, 9])
    with col1:
        if st.button("🤖 IA - AFB", use_container_width=True):
            st.session_state.active_input = ""
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    # --------------- CONTENU PRINCIPAL --------------
    st.markdown("""
        <style>
            .chat-container {
                max-width: 900px;
                margin: auto;
                padding: 30px 20px;
            }
            .element-container:has(input) input {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
            }
            .stButton button {
                background-color: red;
                border: none;
                color: white;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 18px;
                cursor: pointer;
            }
        </style>
        <div class="chat-container">
    """, unsafe_allow_html=True)

    if st.session_state.active_input:
        st.info(f"**Dernière question :** {st.session_state.active_input}")

    #st.download_button("📥 Télécharger",
                       #data=st.session_state.active_input.encode(),
                       #file_name="question.txt")

    # Zone de saisie + bouton ➤ à droite
    with st.form("form_input", clear_on_submit=True):
        col1, col2 = st.columns([6, 1])
        with col1:
            user_input = st.text_input("Pose ta question à l'IA ici...", value="", label_visibility="collapsed")
        with col2:
            submitted = st.form_submit_button("➤")
        st.markdown('</div></div>', unsafe_allow_html=True)

        if submitted and user_input.strip():
            st.session_state.active_input = user_input.strip()
            st.session_state.history.append(user_input.strip())
            st.rerun()

# ------------------ LANCEMENT ------------------
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
