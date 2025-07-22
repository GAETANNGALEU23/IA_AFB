# afriland_app.py
import streamlit as st
from PIL import Image
import datetime

# Simulated user credentials (Replace with real auth logic in backend)
USERS = {
    "user@afriland.cm": "password123",
    "admin@afriland.cm": "adminpass"
}

# Simulated session state setup
def init_session_state():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "email" not in st.session_state:
        st.session_state.email = ""
    if "history" not in st.session_state:
        st.session_state.history = []
    if "active_input" not in st.session_state:
        st.session_state.active_input = ""

# Logo image
@st.cache_resource
def get_logo():
    return Image.open("afriland_logo.png")  # Assure-toi que ce fichier est bien dans ton dossier

# Login page
def login_page():
    st.markdown("""
        <style>
        body {background-color: white;}
        .stButton button {
            background-color: red;
            color: white;
            border: none;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    logo = get_logo()
    st.image(logo, width=150)
    st.markdown("## Connexion à Afriland First Bank")
    email = st.text_input("Adresse email (domaine @afriland.cm)", value="")
    password = st.text_input("Mot de passe", type="password")
    
    if st.button("Connexion"):
        if email in USERS and USERS[email] == password:
            st.session_state.authenticated = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Email ou mot de passe incorrect.")

# Main page
def main_page():
    st.set_page_config(layout="wide")

    with st.sidebar:
        st.image(get_logo(), width=100)
        st.markdown("### Historique")
        for idx, hist in enumerate(st.session_state.history[::-1]):
            if st.button(f"🔁 {hist[:20]}...", key=f"hist_{idx}"):
                st.session_state.active_input = hist
                st.rerun()

    # Custom styles
    st.markdown("""
        <style>
        .main-container {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 10px;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 10px;
            border-bottom: 2px solid #ccc;
        }
        .header h3 {
            color: black;
        }
        .logout {
            background-color: red;
            color: white;
            font-weight: bold;
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
        }
        .info-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            min-height: 200px;
        }
        .chat-input-container {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 0px 6px rgba(0,0,0,0.1);
            margin-top: 30px;
        }
        textarea {
            border-radius: 10px !important;
            padding: 10px;
            font-size: 16px;
        }
        .submit-button {
            float: right;
            margin-top: 10px;
            background-color: red;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 8px 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown(f"""
    <div class="header">
        <h3>{st.session_state.email}</h3>
        <form action="" method="post"><button class="logout" type="submit" name="logout">Déconnexion</button></form>
    </div>
    """, unsafe_allow_html=True)

    if "logout" in st.session_state:
        st.session_state.authenticated = False
        st.rerun()

    st.markdown("<h2 style='color: red;'>FIRST BANK - IA</h2>", unsafe_allow_html=True)

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    # Info display
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    if st.session_state.active_input:
        st.markdown(f"**📝 Dernière saisie :** {st.session_state.active_input}")
    else:
        st.markdown("*Aucune donnée disponible.*")
    st.download_button("📥 Télécharger", data=st.session_state.active_input.encode(), file_name="info.txt")
    st.markdown("</div>", unsafe_allow_html=True)

    # Input zone façon ChatGPT
    st.markdown("<div class='chat-input-container'>", unsafe_allow_html=True)
    input_text = st.text_area("💬 Posez votre question ici", value=st.session_state.active_input, height=120, label_visibility="collapsed")
    
    if st.button("🚀 Envoyer", key="submit_btn"):
        if input_text.strip():
            st.session_state.history.append(input_text.strip())
            st.session_state.active_input = input_text.strip()
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Entry point
init_session_state()
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
