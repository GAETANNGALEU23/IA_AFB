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
        with st.expander("👤", expanded=False):
            st.markdown(f"**{st.session_state.email}**")
            if st.button("🔓 Déconnexion"):
                st.session_state.authenticated = False
                st.session_state.email = ""
                st.rerun()

    # ---------------- Header ----------------
    st.markdown(f"""
        <div style='display: flex; flex-direction: column; align-items: center;
                    padding: 12px 25px; background-color: #f9f9f9; border-bottom: 1px solid #ddd;'>
            <h2 style='color: red;'>🤖 AFRILAND IA</h2>
            <h3 style='color: red; margin-top: -15px;'>IA - FIRST BANK</h3>
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
