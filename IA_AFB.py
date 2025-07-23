import streamlit as st

# ------------------ CONFIGURATION ------------------
st.set_page_config(page_title="AFRILAND IA", layout="centered")

# ------------------ CREDENTIELS SIMULÉS ------------------
USERS = {
    "user@afriland.cm": "password123",
    "admin@afriland.cm": "adminpass"
}

# ------------------ SESSION ------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "email" not in st.session_state:
    st.session_state.email = ""

# ------------------ PAGE DE CONNEXION ------------------
def login_page():
    st.markdown("""
        <style>
            .login-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 75vh;
            }
            .login-box {
                background-color: white;
                padding: 40px 30px;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-container"><div class="login-box">', unsafe_allow_html=True)
    st.title("Connexion IA")

    email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm")
    password = st.text_input("Mot de passe", type="password")

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
    st.success(f"Bienvenue, {st.session_state.email} ! 🎉")
    st.write("Ceci est la page principale.")

# ------------------ ROUTAGE ------------------
if not st.session_state.authenticated:
    login_page()
else:
    main_page()
