def login_page():
    # CSS pour la mise en page
    st.markdown("""
        <style>
            .full-page {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f2f6;
            }
            .login-box {
                background-color: white;
                padding: 40px 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                max-width: 400px;
                width: 100%;
                text-align: center;
            }
            .login-title {
                font-size: 22px;
                color: #d40000;
                margin-bottom: 25px;
                font-weight: bold;
            }
            .stButton>button {
                background-color: #d40000;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 30px;
                width: 100%;
            }
        </style>
    """, unsafe_allow_html=True)

    # Layout principal centré
    with st.container():
        st.markdown('<div class="full-page"><div class="login-box">', unsafe_allow_html=True)
        
        st.image(get_logo(), width=120)
        st.markdown('<div class="login-title">CONNEXION IA - FIRST BANK</div>', unsafe_allow_html=True)

        email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm")
        password = st.text_input("Mot de passe", type="password")

        login = st.button("Connexion")
        if login:
            if email in USERS and USERS[email] == password:
                st.session_state.authenticated = True
                st.session_state.email = email
                st.rerun()
            else:
                st.error("Email ou mot de passe incorrect.")

        st.markdown('</div></div>', unsafe_allow_html=True)
