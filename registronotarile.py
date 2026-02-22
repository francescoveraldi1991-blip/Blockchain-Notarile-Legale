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
st.title("⚖️ Piattaforma Notarile Blockchain 3.0")
st.sidebar.header("Menu Funzioni")
scelta = st.sidebar.radio("Cosa vuoi fare?", 
                         ["Notarizza Contratto/PDF", "Ricerca per Codice Fiscale", "Gestisci Testamenti/Revoche", "Registro Completo"])

# --- 1. CARICAMENTO PDF CON CODICE FISCALE ---
if scelta == "Notarizza Contratto/PDF":
    st.header("📄 Notarizzazione Documentale")
    col1, col2 = st.columns(2)
    with col1:
        nome_atto = st.text_input("Identificativo Atto (es. Repertorio n.)")
        cf_soggetto = st.text_input("Codice Fiscale del Soggetto (Testatore/Contraente)").upper()
    with col2:
        file_caricato = st.file_uploader("Carica il file PDF", type=["pdf"])
    
    if st.button("Registra su Blockchain"):
        if file_caricato and nome_atto and cf_soggetto:
            bytes_data = file_caricato.getvalue()
            impronta = calcola_hash(bytes_data)
            
            nuovo_blocco = {
                "indice": len(st.session_state.blockchain) + 1,
                "nome": nome_atto,
                "cf": cf_soggetto,
                "data": datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
                "hash": impronta,
                "stato": "Valido"
            }
            st.session_state.blockchain.append(nuovo_blocco)
            st.success(f"Atto '{nome_atto}' legato al CF {cf_soggetto} registrato!")
        else:
            st.error("Compila tutti i campi obbligatori.")

# --- 2. NUOVA FUNZIONE: RICERCA PER CODICE FISCALE ---
elif scelta == "Ricerca per Codice Fiscale":
    st.header("🔍 Archivio Storico per Soggetto")
    search_cf = st.text_input("Inserisci il Codice Fiscale da ricercare").upper()
    
    if search_cf:
        risultati = [b for b in st.session_state.blockchain if b['cf'] == search_cf]
        if risultati:
            st.write(f"Trovati {len(risultati)} atti per il soggetto {search_cf}:")
            for r in risultati:
                with st.expander(f"Atto: {r['nome']} - Stato: {r['stato']}"):
                    st.write(f"**Data Certa:** {r['data']}")
                    st.write(f"**Impronta Digitale:** `{r['hash']}`")
        else:
            st.info("Nessun atto trovato per questo Codice Fiscale.")

# --- 3. GESTIONE TESTAMENTI E REVOCHE ---
elif scelta == "Gestisci Testamenti/Revoche":
    st.header("📝 Gestione Successioni Digitali")
    atti_validi = [b['nome'] for b in st.session_state.blockchain if b['stato'] == "Valido"]
    
    if atti_validi:
        atto_da_revocare = st.selectbox("Seleziona Atto da Revocare", atti_validi)
        if st.button("Esegui Revoca Formale"):
            for b in st.session_state.blockchain:
                if b['nome'] == atto_da_revocare:
                    b['stato'] = f"REVOCATO il {datetime.datetime.now().strftime('%d/%m/%Y')}"
            st.warning(f"L'atto '{atto_da_revocare}' è stato invalidato.")
    else:
        st.write("Nessun atto valido disponibile per la revoca.")

# --- 4. REGISTRO COMPLETO ---
elif scelta == "Registro Completo":
    st.header("📜 Libro Mastro Immutabile")
    if st.session_state.blockchain:
        st.table(pd.DataFrame(st.session_state.blockchain))
    else:
        st.write("Il registro è ancora vuoto.")
