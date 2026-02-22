# --- AGGIUNTA AL MENU SIDEBAR ---
# scelta = st.sidebar.radio(..., ["..., "Crea Smart Contract"])

# --- 5. FUNZIONE SMART CONTRACT (LOGICA AUTO-ESECUTIVA) ---
if scelta == "Crea Smart Contract":
    st.header("⚙️ Configurazione Smart Contract")
    st.info("Qui puoi programmare clausole che si eseguono automaticamente.")
    
    tipo_smart = st.selectbox("Tipo di Contratto", ["Deposito in Garanzia (Escrow)", "Eredità Digitale"])
    
    col1, col2 = st.columns(2)
    with col1:
        beneficiario = st.text_input("Codice Fiscale Beneficiario").upper()
        scadenza = st.date_input("Data di sblocco/verifica")
    with col2:
        valore = st.number_input("Valore vincolato (€)", min_value=0.0)
    
    if st.button("Attiva Smart Contract"):
        if beneficiario and valore > 0:
            st.success(f"Smart Contract Attivato!")
            st.code(f"""
            // Logica generata:
            IF (Data_Attuale >= {scadenza}) AND (Evento_Confermato) 
            THEN Sblocca {valore}€ a favore di {beneficiario}
            ELSE Mantieni vincolato su indirizzo Blockchain.
            """)
            
            # Salviamo lo smart contract nel registro
            st.session_state.blockchain.append({
                "indice": len(st.session_state.blockchain) + 1,
                "nome": f"SMART: {tipo_smart}",
                "cf": beneficiario,
                "data": datetime.datetime.now().strftime("%d/%m/%Y"),
                "hash": "LOGICA_PROGRAMMATA",
                "stato": "IN ATTESA"
            })
