# ------------------ PAGE DE CONNEXION ------------------
def login_page():
    st.markdown("""
        <style>
            /* Overlay de fond */
            .overlay {
                position: fixed;
                top: 0; left: 0;
                width: 100%; height: 100%;
                background-color: rgba(0, 0, 0, 0.6);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
            }

            /* Carte centrale (la popup) */
            .login-popup {
                background-color: white;
                padding: 40px 30px;
                border-radius: 16px;
                box-shadow: 0 0 25px rgba(0, 0, 0, 0.3);
                text-align: center;
                width: 100%;
                max-width: 400px;
            }

            .login-popup h2 {
                color: #d10000;
                margin-bottom: 20px;
            }

            .stTextInput > div > input {
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #ccc;
                width: 100%;
            }

            .stTextInput {
                margin-bottom: 20px;
            }

            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 20px;
                width: 100%;
            }

            /* Cache le reste de la page (barres, etc.) */
            header, footer, .stSidebar {
                display: none !important;
            }
        </style>

        <div class="overlay">
            <div class="login-popup">
                <img src="https://i.ibb.co/ZGr9F67/afriland-logo-small.png" width="100"/>
                <h2>Connexion AFRILAND IA</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Utiliser des conteneurs invisibles pour s’injecter dans la popup
    col1, col2, col3 = st.columns([3, 6, 3])
    with col2:
        email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm", label_visibility="collapsed")
        password = st.text_input("Mot de passe", type="password", label_visibility="collapsed")
        if st.button("Connexion"):
            if email in USERS and USERS[email] == password:
                st.session_state.authenticated = True
                st.session_state.email = email
                st.rerun()
            else:
                st.error("Email ou mot de passe incorrect.")
