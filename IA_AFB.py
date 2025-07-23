import streamlit as st
from PIL import Image
import datetime
import io
import base64

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
def get_logo():
    try:
        # Solution alternative avec un logo intégré en base64 si le fichier n'est pas trouvé
        logo_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AkEEjUXFv7Z3QAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAAFUlEQVQ4y2NgGAWjYBSMglEwCkbBKBgFQwUAATYAh8Qn4h0AAAAASUVORK5CYII="
        logo_bytes = base64.b64decode(logo_base64)
        return Image.open(io.BytesIO(logo_bytes))
    except Exception as e:
        st.error(f"Erreur de chargement du logo: {e}")
        # Retourne une image vide si le logo n'est pas trouvé
        return Image.new('RGB', (150, 150), color='red')

# ------------------ PAGE DE CONNEXION ------------------
def login_page():
    st.markdown("""
        <style>
            .login-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 80vh;
                gap: 20px;
            }
            .stButton button {
                background-color: #d40000;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 20px;
                border: none;
                width: 100%;
            }
            .stTextInput input, .stTextInput input:focus {
                border-radius: 8px;
                padding: 10px;
                border: 1px solid #ddd;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # Logo centré
        st.image(get_logo(), width=150)
        
        # Formulaire de connexion
        st.markdown("## CONNEXION IA - FIRST BANK")
        email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_password")
        
        if st.button("Connexion", key="login_button"):
            if email in USERS and USERS[email] == password:
                st.session_state.authenticated = True
                st.session_state.email = email
                st.rerun()
            else:
                st.error("Email ou mot de passe incorrect.")
        
        st.markdown('</div>', unsafe_allow_html=True)

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
        
        # Email et bouton de déconnexion alignés
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"👤 **{st.session_state.email}**")
        with col2:
            if st.button("🔓", key="logout_btn"):
                st.session_state.authenticated = False
                st.session_state.email = ""
                st.session_state.history = []
                st.rerun()

    # ---------------- En-tête ----------------
    st.markdown(f"""
        <div style='display: flex; justify-content: space-between; align-items: center; 
                    padding: 10px 20px; background-color: #f9f9f9; border-bottom: 1px solid #ddd;'>
            <h2 style='color: #d40000;'>🤖 AFRILAND IA</h2>
            <div style='display: flex; align-items: center; gap: 10px;'>
                <span style='font-weight: bold;'>{st.session_state.email}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ---------------- Zone réponse ----------------
    if st.session_state.active_input:
        st.info(f"**Dernière question :** {st.session_state.active_input}")
    else:
        st.info("Prêt à répondre à vos questions.")

    st.download_button("📥 Télécharger la dernière saisie",
                      data=st.session_state.active_input.encode() if st.session_state.active_input else b"",
                      file_name="question_afriland.txt",
                      disabled=not st.session_state.active_input)

    # ---------------- Zone de saisie ----------------
    st.markdown("""
        <style>
            .stTextArea textarea {
                border-radius: 8px;
                padding: 15px;
                border: 1px solid #ddd !important;
                box-shadow: none !important;
            }
            .stTextArea div[data-baseweb="input"] {
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .send-arrow {
                position: absolute;
                right: 15px;
                bottom: 15px;
                color: #d40000;
                font-size: 24px;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.form(key="question_form"):
        user_input = st.text_area("", 
                                value=st.session_state.active_input, 
                                height=150, 
                                label_visibility="collapsed",
                                placeholder="Entrez votre question ici...",
                                key="question_input")
        
        # Flèche de soumission stylisée
        st.markdown("""
            <button type="submit" class="send-arrow" style="background: none; border: none;">➤</button>
        """, unsafe_allow_html=True)
        
        if st.form_submit_button("", key="submit_question"):
            if user_input.strip():
                st.session_state.history.append(user_input.strip())
                st.session_state.active_input = user_input.strip()
                st.rerun()

# ------------------ LANCEMENT ------------------
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
