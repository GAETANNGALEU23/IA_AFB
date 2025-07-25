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
            body {
                background-color: #f7f9fc;
            }

            .login-container {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                animation: fadeIn 1.2s ease-in;
                background: linear-gradient(135deg, #f8f9fb 0%, #edf1f5 100%);
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .login-box {
                background-color: #ffffff;
                padding: 40px 30px;
                border-radius: 16px;
                box-shadow: 0 4px 18px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 400px;
                text-align: center;
                transition: all 0.3s ease;
            }

            .login-box:hover {
                box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12);
            }

            .login-title {
                color: #c40000;
                font-size: 24px;
                font-weight: 700;
                margin-bottom: 30px;
            }

            .stTextInput > div > div > input {
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #ccc;
            }

            .stTextInput > div {
                margin-bottom: 20px;
            }

            .stButton > button {
                background-color: #c40000;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 10px;
                padding: 12px 24px;
                width: 100%;
                font-size: 16px;
                transition: background-color 0.3s ease;
            }

            .stButton > button:hover {
                background-color: #a00000;
            }

            .logo-img {
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-container"><div class="login-box">', unsafe_allow_html=True)

    st.image(get_logo(), width=100)
    st.markdown('<div class="login-title">CONNEXION IA - FIRST BANK</div>', unsafe_allow_html=True)

    email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm")
    password = st.text_input("Mot de passe", placeholder="Entrez votre mot de passe", type="password")

    if st.button("Connexion"):
        if email in USERS and USERS[email] == password:
            st.session_state.authenticated = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Email ou mot de passe incorrect.")

    st.markdown('</div></div>', unsafe_allow_html=True)


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
        
        # Espace pour pousser le menu utilisateur en bas
        st.markdown("---")
        
        # Menu utilisateur en bas de la sidebar
        with st.expander("👤 My Profile", expanded=False):
            st.markdown(f"**{st.session_state.email}**")
            if st.button("🔓 Déconnexion"):
                st.session_state.authenticated = False
                st.session_state.email = ""
                st.rerun()

    # ---------------- Header ----------------
    st.markdown(f"""
        <div style='display: flex; justify-content: space-between; align-items: center;
                    padding: 12px 25px; background-color: #f9f9f9; border-bottom: 1px solid #ddd;'>
             <h2 style='color: red;'>🤖 AFRILAND - IA</h2>
        </div>
    """, unsafe_allow_html=True)

    # ---------------- Main Content ----------------
    st.markdown("""
        <style>
            .chat-container {
                max-width: 900px;
                margin: auto;
                padding: 30px 20px;
            }
            .input-box {
                display: flex;
                align-items: center;
                gap: 10px;
                background-color: #f0f2f6;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
            }
            .input-box textarea {
                flex: 1;
                border: none;
                resize: none;
                background-color: transparent;
                font-size: 16px
                padding-top: 10px;
            }
            .input-box button {
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

    st.download_button("📥 Télécharger",
                       data=st.session_state.active_input.encode(),
                       file_name="question.txt")

    # Zone de saisie (type ChatGPT)
    with st.form("form_input", clear_on_submit=True):
        user_input = st.text_area("", value="", height=80, label_visibility="collapsed")
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
