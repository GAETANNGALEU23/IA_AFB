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

            /* Fenêtre popup */
            .login-popup {
                background-color: white;
                padding: 30px 25px;
                border-radius: 16px;
                box-shadow: 0 0 25px rgba(0, 0, 0, 0.3);
                text-align: center;
                width: 100%;
                max-width: 320px;
            }

            .login-popup h2 {
                color: #d10000;
                margin-bottom: 25px;
                font-size: 20px;
            }

            .stTextInput > div > input {
                padding: 8px;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 14px;
            }

            .stTextInput {
                margin-bottom: 15px;
            }

            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 0;
                width: 100%;
                font-size: 14px;
            }

            header, footer, .stSidebar {
                display: none !important;
            }
        </style>

        <div class="overlay">
            <div class="login-popup">
                <img src="https://i.ibb.co/ZGr9F67/afriland-logo-small.png" width="80"/>
                <h2>Connexion AFRILAND IA</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Conteneur invisible pour insérer les champs dans le centre
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
