def login_page():
    # Appliquer un style global pour centrer le formulaire
    st.markdown("""
        <style>
            .login-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 80vh;
                background-color: #f5f5f5;
            }
            .login-box {
                background-color: white;
                padding: 40px 30px;
                border-radius: 12px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
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

    # Structure centrée
    st.markdown('<div class="login-container"><div class="login-box">', unsafe_allow_html=True)
    
    st.image(get_logo(), width=100)
    st.markdown("## CONNEXION IA")

    email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm")
    password = st.text_input("Mot de passe", type="password", placeholder="Votre mot de passe")

    if st.button("Connexion"):
        if email in USERS and USERS[email] == password:
            st.session_state.authenticated = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Email ou mot de passe incorrect.")

    st.markdown('</div></div>', unsafe_allow_html=True)
