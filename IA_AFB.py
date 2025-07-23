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
    if "history" not in st.session_state:
        st.session_state.history = []
    if "active_input" not in st.session_state:
        st.session_state.active_input = ""
    if "new_input" not in st.session_state:
        st.session_state.new_input = ""

init_session_state()

# ------------------ LOGO ------------------
@st.cache_resource
def get_logo():
    return Image.open("afriland_logo_1.png")

# ------------------ PAGE DE CONNEXION ------------------
def login_page():
    st.markdown("""
        <style>
            html, body, [data-testid="stApp"] {
                height: 100%;
                margin: 0;
                padding: 0;
                background-color: #f0f2f6;
            }

            .login-container {
                position: fixed;
                top: 0;
                left: 0;
                height: 100vh;
                width: 100vw;
                background-color: rgba(0, 0, 0, 0.5);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 9999;
            }

            .login-box {
                background-color: white;
                padding: 40px 30px;
                border-radius: 12px;
                box-shadow: 0 0 25px rgba(0, 0, 0, 0.3);
                text-align: center;
                width: 100%;
                max-width: 400px;
            }

            .login-box h2 {
                color: #b00000;
                margin-bottom: 25px;
            }

            .stTextInput input {
                text-align: center;
            }

            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 30px;
                margin-top: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Boîte d'authentification
    with st.container():
        st.markdown('<div class="login-container"><div class="login-box">', unsafe_allow_html=True)
        st.image(get_logo(), width=100)
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

        st.markdown("</div></div>", unsafe_allow_html=True)

# ------------------ PAGE PRINCIPALE ------------------
def main_page():
    with st.sidebar:
        st.image(get_logo(), width=120)
        st.markdown("### Historique")
        for idx, hist in enumerate(st.session_state.history[::-1]):
            if st.button(f"🕘 {hist[:25]}...", key=f"hist_{idx}"):
                st.session_state.active_input = hist
                st.rerun()
        st.markdown("---")

    st.markdown(f"""
        <div style='display: flex; justify-content: space-between; align-items: center;
                    padding: 12px 25px; background-color: #f9f9f9; border-bottom: 1px solid #ddd;'>
            <h2 style='color: red;'>🤖 AFRILAND IA</h2>
            <div style='display: flex; align-items: center; gap: 20px;'>
                <span style='font-weight: bold;'>👤 {st.session_state.email}</span>
                <form action="" method="post">
                    <button style='background-color: red; color: white; border: none; padding: 8px 18px; 
                                   border-radius: 8px; cursor: pointer;' 
                            onClick="window.location.reload();">
                        🔓 Déconnexion
                    </button>
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("Bienvenue dans l'interface IA.")

# ------------------ LANCEMENT ------------------
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
