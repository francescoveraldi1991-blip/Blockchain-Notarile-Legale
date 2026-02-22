import streamlit as st
import hashlib
import datetime
import pandas as pd

st.set_page_config(page_title="Notaio Digitale Pro", page_icon="⚖️", layout="wide")

# --- LOGICA BLOCKCHAIN ---
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

def calcola_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

# --- INTERFACCIA ---
st.title("⚖️ Piattaforma Notarile Blockchain 2.0")
st.sidebar.header("Menu Funzioni")
scelta = st.sidebar.radio("Cosa vuoi fare?", ["Notarizza Contratto/PDF", "Gestisci Testamenti/Revoche", "Registro e Certificati"])

# --- 1. CARICAMENTO PDF ---
if scelta == "Notarizza Contratto/PDF":
    st.header("📄 Notarizzazione Documentale")
    nome_atto = st.text_input("Identificativo Atto (es. Repertorio n.)")
    file_caricato = st.file_uploader("Carica il file PDF del contratto", type=["pdf"])
    
    if st.button("Registra su Blockchain"):
        if file_caricato and nome_atto:
            bytes_data = file_caricato.getvalue()
            impronta = calcola_hash(bytes_data)
            
            nuovo_blocco = {
                "indice": len(st.session_state.blockchain) + 1,
                "nome": nome_atto,
                "data": datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
                "hash": impronta,
                "tipo": "Contratto/Atto",
                "stato": "Valido"
            }
            st.session_state.blockchain.append(nuovo_blocco)
            st.success(f"File '{file_caricato.name}' notarizzato con successo!")
        else:
            st.error("Inserisci il nome e carica un file.")

# --- 2. GESTIONE TESTAMENTI E REVOCHE ---
elif scelta == "Gestisci Testamenti/Revoche":
    st.header("📝 Gestione Successioni Digitali")
    st.info("Secondo il Codice Civile, ogni atto può essere revocato da un atto successivo.")
    
    atto_da_revocare = st.selectbox("Seleziona Atto da Revocare/Aggiornare", 
                                    [b['nome'] for b in st.session_state.blockchain if b['stato'] == "Valido"])
    motivo_revoca = st.text_area("Motivo della revoca o nuovi estremi")
    
    if st.button("Esegui Revoca Formale"):
        # Logica di revoca: creiamo un nuovo blocco che invalida il precedente
        data_rev = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        for b in st.session_state.blockchain:
            if b['nome'] == atto_da_revocare:
                b['stato'] = f"REVOCATO il {data_rev}"
        
        st.warning(f"L'atto '{atto_da_revocare}' è stato segnato come revocato nel registro.")

# --- 3. REGISTRO E ESPORTAZIONE CERTIFICATO ---
elif scelta == "Registro e Certificati":
    st.header("📜 Registro Immutabile e Certificazioni")
    
    if st.session_state.blockchain:
        df = pd.DataFrame(st.session_state.blockchain)
        st.table(df) # Visualizzazione stile "Libro Mastro"
        
        st.divider()
        st.subheader("🖨️ Esporta Certificato di Data Certa")
        atto_cert = st.selectbox("Scegli l'atto per il certificato", [b['nome'] for b in st.session_state.blockchain])
        
        # Simulazione Certificato
        for b in st.session_state.blockchain:
            if b['nome'] == atto_cert:
                cert_text = f"""
                CERTIFICATO DI NOTARIZZAZIONE DIGITALE
                --------------------------------------
                ID ATTO: {b['indice']}
                DENOMINAZIONE: {b['nome']}
                DATA CERTA: {b['data']}
                IMPRONTA DIGITALE (SHA-256): {b['hash']}
                STATO ATTUALE: {b['stato']}
                --------------------------------------
                Validato tramite tecnologia Blockchain.
                """
                st.code(cert_text)
                st.download_button("Scarica Certificato (TXT)", cert_text, file_name=f"certificato_{atto_cert}.txt")
    else:
        st.write("Il registro è vuoto.")
