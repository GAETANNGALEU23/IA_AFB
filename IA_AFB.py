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
    return Image.open("afriland_logo.png")  # Place logo file in project folder

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
        .header .logout {
            background-color: red;
            color: white;
            font-weight: bold;
        }
        .info-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            min-height: 200px;
        }
        </style>
    """, unsafe_allow_html=True)

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

    # Input zone
    st.markdown("---")
    input_text = st.text_area("Zone de saisie", value=st.session_state.active_input, height=150)
    if st.button("Soumettre"):
        if input_text:
            st.session_state.history.append(input_text)
            st.session_state.active_input = input_text
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# Entry point
init_session_state()
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
