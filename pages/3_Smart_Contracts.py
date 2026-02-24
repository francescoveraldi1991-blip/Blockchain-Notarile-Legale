# ... (parte iniziale del design invariata) ...

with col_setup:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    st.subheader("🛠️ Configura Smart Contract")
    
    with st.form("sc_form", clear_on_submit=True):
        nome_contratto = st.text_input("Oggetto dell'Accordo")
        beneficiario = st.text_input("Beneficiario della Prestazione (ID/Wallet)")
        
        # CAMBIO LOGICA: Da Soldi a Prestazione Digitale
        tipo_output = st.selectbox("Controprestazione Automatica", [
            "Emissione Certificato di Conformità (NFT)",
            "Sblocco Accesso Documentazione Protetta",
            "Notifica Immutabile di Adempimento",
            "Aggiornamento Rating Fornitore"
        ])
        
        scadenza = st.date_input("Termine Adempimento", datetime.date.today() + datetime.timedelta(days=15))
        
        st.markdown("<br>", unsafe_allow_html=True)
        attivazione = st.form_submit_button("DEPLOYA SU BLOCKCHAIN")
        
        if attivazione and nome_contratto:
            nuovo_sc = {
                "id": hashlib.md5(nome_contratto.encode()).hexdigest()[:6].upper(),
                "nome": nome_contratto,
                "beneficiario": beneficiario,
                "output": tipo_output,
                "scadenza": scadenza.strftime("%d/%m/%Y"),
                "stato": "ACTIVE",
                "completato": False
            }
            st.session_state.smart_contracts.append(nuovo_sc)
            st.success(f"Contract SC-{nuovo_sc['id']} deployato sulla rete.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_monitor:
    st.subheader("📡 Status Contratti On-Chain")
    
    for idx, sc in enumerate(st.session_state.smart_contracts):
        badge_class = "status-completed" if sc['completato'] else "status-active"
        status_text = "ESECUTO / CERTIFICATO EMESSO" if sc['completato'] else "IN ATTESA DI INPUT"
        
        st.markdown(f"""
        <div class="notary-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin:0;">{sc['nome']}</h4>
                <span class="{badge_class}">{status_text}</span>
            </div>
            <p style="font-size: 0.9rem; margin-top: 10px;">
                <b>Beneficiario:</b> {sc['beneficiario']}<br>
                <b>Azione Automatica:</b> {sc['output']}<br>
                <b>Scadenza:</b> {sc['scadenza']}
            </p>
        """, unsafe_allow_html=True)
        
        if not sc['completato']:
            file_verbale = st.file_uploader(f"Carica prova adempimento per {sc['id']}", type=["pdf"], key=f"sc_{sc['id']}")
            if file_verbale:
                st.session_state.smart_contracts[idx]['completato'] = True
                st.rerun()
        else:
            # MOSTRA IL RISULTATO DELLA CONTROPRESTAZIONE
            st.markdown(f"""
                <div style="background: #e8f5e9; padding: 10px; border-radius: 10px; border: 1px solid #2e7d32;">
                    <p style="margin:0; color: #2e7d32; font-size: 0.8rem;">
                        <b>Smart Contract Executed:</b><br>
                        L'azione "{sc['output']}" è stata registrata permanentemente. <br>
                        Transaction Hash: {hashlib.sha256(sc['nome'].encode()).hexdigest()[:32]}...
                    </p>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
