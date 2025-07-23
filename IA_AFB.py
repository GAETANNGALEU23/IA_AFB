def login_page():
    st.markdown(
        <style>
            html, body, [class*="css"] {
                height: 100%;
                margin: 0;
                padding: 0;
                background-color: #f2f2f2;
            }
            .login-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
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
            .login-box img {
                margin-bottom: 20px;
            }
            .login-title {
                font-size: 22px;
                color: #d40000;
                margin-bottom: 25px;
                font-weight: bold;
            }
            .stTextInput>div>div>input {
                text-align: center;
            }
            .stButton button {
                background-color: #d40000;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 10px 30px;
                margin-top: 10px;
                width: 100%;
            }
        </style>
        <div class="login-container">
            <div class="login-box">
    """, unsafe_allow_html=True)

    st.image(get_logo(), width=120)
    st.markdown('<div class="login-title">CONNEXION IA - FIRST BANK</div>', unsafe_allow_html=True)

    email = st.text_input("Adresse email", placeholder="votre.email@afriland.cm")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Connexion"):
        if email in USERS and USERS[email] == password:
            st.session_state.authenticated = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Email ou mot de passe incorrect.")

    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)
