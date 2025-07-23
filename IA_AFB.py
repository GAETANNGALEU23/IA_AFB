def login_page():
    st.markdown("""
        <style>
            /* Fond d'écran semi-transparent */
            .overlay {
                position: fixed;
                top: 0; left: 0;
                width: 100%; height: 100%;
                background-color: rgba(0, 0, 0, 0.6);
                z-index: 9999;
            }

            /* Boîte centrale */
            .login-container {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: white;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 0 25px rgba(0,0,0,0.3);
                width: 100%;
                max-width: 340px;
                z-index: 10000;
                text-align: center;
            }

            .login-container h2 {
                color: #d10000;
                margin-bottom: 20px;
                font-size: 20px;
            }

            .stTextInput > div > input {
                padding: 8px;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 14px;
            }

            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px;
                width: 100%;
                font-size: 14px;
            }

            header, footer, .stSidebar {
                display: none !important;
            }
        </style>
        <div class="overlay"></div>
    """, unsafe_allow_html=True)

    # Le contenu réel de la popup (centré via Streamlit)
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.image("afriland_logo_1.png", width=80)
        st.markdown('<h2>Connexion AFRILAND IA</h2>', unsafe_allow_html=True)

        email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm", label_visibility="collapsed")
        password = st.text_input("Mot de passe", type="password", label_visibility="collapsed")

        if st.button("Connexion"):
            if email in USERS and USERS[email] == password:
                st.session_state.authenticated = True
                st.session_state.email = email
                st.rerun()
            else:
                st.error("Email ou mot de passe incorrect.")

        st.markdown("</div>", unsafe_allow_html=True)
