# ------------------ PAGE DE CONNEXION STYLE POPUP ------------------
def login_page():
    st.markdown("""
        <style>
            /* Fond principal semi-transparent */
            .main {
                background-color: rgba(0, 0, 0, 0.5) !important;
            }
            
            /* Conteneur du popup */
            .login-popup {
                position: relative;
                max-width: 400px;
                margin: 100px auto 0;
                padding: 2.5rem;
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                animation: fadeIn 0.3s ease-out;
            }
            
            /* Animation d'apparition */
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            /* Style du logo */
            .login-logo {
                margin: 0 auto 1.5rem;
                display: block;
                width: 120px;
            }
            
            /* Titre */
            .login-title {
                color: #d40000;
                text-align: center;
                font-size: 1.5rem;
                margin-bottom: 1.8rem;
                font-weight: 600;
            }
            
            /* Champs de formulaire */
            .stTextInput input {
                border: 1px solid #ddd !important;
                border-radius: 8px !important;
                padding: 12px 15px !important;
                margin-bottom: 1rem;
            }
            
            /* Bouton de connexion */
            .stButton button {
                width: 100%;
                background-color: #d40000 !important;
                color: white !important;
                font-weight: 600 !important;
                border-radius: 8px !important;
                padding: 12px 0 !important;
                margin-top: 10px;
                border: none !important;
                transition: all 0.3s;
            }
            
            .stButton button:hover {
                background-color: #b30000 !important;
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            
            /* Pied de page */
            .login-footer {
                text-align: center;
                margin-top: 1.5rem;
                color: #666;
                font-size: 0.8rem;
            }
            
            /* Message d'erreur */
            .stAlert {
                border-radius: 8px !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Structure HTML du popup
    st.markdown("""
        <div class="login-popup">
            <img src="https://www.afrilandfirstbank.com/wp-content/uploads/2021/06/logo-afriland-first-bank.png" class="login-logo">
            <h2 class="login-title">Connexion Sécurisée</h2>
    """, unsafe_allow_html=True)
    
    # Champs de formulaire
    email = st.text_input("", placeholder="Adresse email professionnelle", key="login_email")
    password = st.text_input("", type="password", placeholder="Mot de passe", key="login_password")
    
    # Bouton de connexion
    if st.button("Se connecter", key="login_button"):
        if email in USERS and USERS[email] == password:
            st.session_state.authenticated = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Identifiants incorrects. Veuillez réessayer.")
    
    # Pied de page
    st.markdown("""
            <p class="login-footer">
                Système sécurisé © 2023 Afriland First Bank<br>
                <em>Vos informations sont cryptées</em>
            </p>
        </div>
    """, unsafe_allow_html=True)

# ------------------ PAGE DE CONNEXION ------------------
def login_page():
    st.markdown("""
        <style>
            .centered {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: start
                padding-top: 100px;
                text-align: center;
            }
            .stButton button {
                background-color: red;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 30px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.image(get_logo(), width=180)
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
    st.markdown('</div>', unsafe_allow_html=True)
# ------------------ PAGE PRINCIPALE ------------------
def main_page():
    # ---------------- Sidebar ----------------
    with st.sidebar:
        st.image(get_logo(), width=120)
        st.markdown("### Historique")
        for idx, hist in enumerate(st.session_state.history[::-1]):
            if st.button(f"🕘 {hist[:25]}...", key=f"hist_{idx}"):
                st.session_state.active_input = hist
                st.rerun()
        
        # Espace pour pousser le menu utilisateur en bas
        st.markdown("---")
        
        # Menu utilisateur en bas de la sidebar
        with st.expander("👤 My Profile", expanded=False):
            st.markdown(f"**{st.session_state.email}**")
            if st.button("🔓 Déconnexion"):
                st.session_state.authenticated = False
                st.session_state.email = ""
                st.rerun()

    # ---------------- Header ----------------
    st.markdown(f"""
        <div style='display: flex; justify-content: space-between; align-items: center;
                    padding: 12px 25px; background-color: #f9f9f9; border-bottom: 1px solid #ddd;'>
           <center> <h2 style='color: red;'>🤖 AFRILAND IA</h2></center>
        </div>
    """, unsafe_allow_html=True)

    # ---------------- Main Content ----------------
    st.markdown("""
        <style>
            .chat-container {
                max-width: 900px;
                margin: auto;
                padding: 30px 20px;
            }
            .input-box {
                display: flex;
                align-items: center;
                gap: 10px;
                background-color: #f0f2f6;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
            }
            .input-box textarea {
                flex: 1;
                border: none;
                resize: none;
                background-color: transparent;
                font-size: 16px
                padding-top: 10px;
            }
            .input-box button {
                background-color: red;
                border: none;
                color: white;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 18px;
                cursor: pointer;
            }
        </style>
        <div class="chat-container">
    """, unsafe_allow_html=True)

    if st.session_state.active_input:
        st.info(f"**Dernière question :** {st.session_state.active_input}")

    st.download_button("📥 Télécharger",
                       data=st.session_state.active_input.encode(),
                       file_name="question.txt")

    # Zone de saisie (type ChatGPT)
    with st.form("form_input", clear_on_submit=True):
        user_input = st.text_area("", value="", height=80, label_visibility="collapsed")
        submitted = st.form_submit_button("➤")
        st.markdown('</div></div>', unsafe_allow_html=True)

        if submitted and user_input.strip():
            st.session_state.active_input = user_input.strip()
            st.session_state.history.append(user_input.strip())
            st.rerun()

# ------------------ LANCEMENT ------------------

if not st.session_state.authenticated:
    login_page()
else:
    main_page()   
