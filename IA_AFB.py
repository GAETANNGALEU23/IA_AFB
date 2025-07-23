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
    if "logout_triggered" not in st.session_state:
        st.session_state.logout_triggered = False

init_session_state()

# ------------------ LOGO AFRILAND ------------------
@st.cache_resource
def get_logo():
    return Image.open("afriland_logo_1.png")  # Assure-toi que ce fichier est bien présent

# ------------------ PAGE DE CONNEXION ------------------
def login_page():
    st.markdown("""
        <style>
            body { background-color: white; }
            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.image(get_logo(), width=150)
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

# ------------------ PAGE PRINCIPALE ------------------
def main_page():
    # ---------------- Sidebar ----------------
    with st.sidebar:
        st.image(get_logo(), width=120)
        st.markdown("### Historique")
        for idx, hist in enumerate(st.session_state.history[::-1]):
            if st.button(f"🕘 {hist[:25]}...", key=f"hist_{idx}"):
                st.session_state.active_input = hist
                st.rerun()
        st.markdown("---")
        st.markdown("👤 **Connecté :**")
        st.markdown(f"{st.session_state.email}")
        if st.button("🔓 Déconnexion"):
            st.session_state.authenticated = False
            st.session_state.email = ""
            st.session_state.history = []
            st.rerun()

    # ---------------- Haut de page ----------------
    st.markdown(f"""
        <div style='display: flex; justify-content: space-between; align-items: center; 
                    padding: 10px 20px; background-color: #f9f9f9; border-bottom: 1px solid #ddd;'>
            <h2 style='color: red;'>🤖 AFRILAND IA</h2>
            <span style='font-weight: bold;'>👤 {st.session_state.email}</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("## 💬 Posez votre question")

    # ---------------- Zone réponse ----------------
    if st.session_state.active_input:
        st.info(f"**Dernière question :** {st.session_state.active_input}")
    else:
        st.info("Aucune question posée pour le moment.")

    st.download_button("📥 Télécharger la dernière saisie",
                       data=st.session_state.active_input.encode(),
                       file_name="question.txt")

    # ---------------- Zone de saisie ----------------
    st.markdown("---")
    user_input = st.text_area("Entrez votre question ici :", 
                              value=st.session_state.active_input, 
                              height=150, label_visibility="collapsed")

    if st.button("🚀 Envoyer"):
        if user_input.strip():
            st.session_state.history.append(user_input.strip())
            st.session_state.active_input = user_input.strip()
            st.success("Question enregistrée.")
            st.rerun()

# ------------------ LANCEMENT ------------------
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
