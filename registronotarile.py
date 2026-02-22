import streamlit as st
import hashlib
import datetime
import pandas as pd

# Configurazione della pagina
st.set_page_config(page_title="Notaio Digitale Pro", page_icon="⚖️", layout="wide")

# --- LOGICA BLOCKCHAIN (Memoria sessione) ---
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

def calcola_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

# --- INTERFACCIA SIDEBAR ---
st.title("⚖️ Piattaforma Notarile Blockchain 4.0")
st.sidebar.header("Menu Funzioni")

# Elenco completo delle funzioni - Assicurati che siano tutte qui!
menu = [
    "Notarizza Contratto/PDF", 
    "Ricerca per Codice Fiscale", 
    "Gestisci Testamenti/Revoche", 
    "Crea Smart Contract",
    "Registro Completo"
]
scelta = st.sidebar.radio("Cosa vuoi fare?", menu)

# --- 1. CARICAMENTO PDF CON CODICE FISCALE ---
if scelta == "Notarizza Contratto/PDF":
    st.header("📄 Notarizzazione Documentale")
    col1, col2 = st.columns(2)
    with col1:
        nome_atto = st.text_input("Identificativo Atto (es. Repertorio n.)")
        cf_soggetto = st.text_input("Codice Fiscale del Soggetto").upper()
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
                "tipo": "Atto PDF",
                "stato": "Valido"
            }
            st.session_state.blockchain.append(nuovo_blocco)
            st.success(f"Atto '{nome_atto}' registrato con successo!")
        else:
            st.error("Per favore, compila tutti i campi.")

# --- 2. RICERCA PER CODICE FISCALE ---
elif scelta == "Ricerca per Codice Fiscale":
    st.header("🔍 Archivio Storico per Soggetto")
    search_cf = st.text_input("Inserisci il Codice Fiscale da ricercare").upper()
    
    if search_cf:
        risultati = [b for b in st.session_state.blockchain if b['cf'] == search_cf]
        if risultati:
            st.write(f"Trovati {len(risultati)} atti per: {search_cf}")
            for r in risultati:
                with st.expander(f"Atto: {r['nome']} - Stato: {r['stato']}"):
                    st.write(f"**Data Certa:** {r['data']}")
                    st.write(f"**Hash:** `{r['hash']}`")
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
            st.warning(f"L'atto '{atto_da_revocare}' è stato invalidato nel registro.")
    else:
        st.write("Nessun atto valido disponibile per la revoca.")

# --- 4. CREAZIONE SMART CONTRACT ---
elif scelta == "Crea Smart Contract":
    st.header("⚙️ Configurazione Smart Contract")
    st.info("Gli Smart Contract hanno valore legale ex Art. 8-ter DL 135/2018.")
    
    tipo_smart = st.selectbox("Tipo di Contratto", ["Eredità Digitale", "Deposito in Garanzia (Escrow)"])
    
    col1, col2 = st.columns(2)
    with col1:
        beneficiario = st.text_input("CF Beneficiario").upper()
        scadenza = st.date_input("Data di sblocco/verifica")
    with col2:
        valore = st.number_input("Valore vincolato (€)", min_value=0.0)
    
    if st.button("Attiva Smart Contract"):
        if beneficiario:
            nuovo_smart = {
                "indice": len(st.session_state.blockchain) + 1,
                "nome": f"SMART: {tipo_smart}",
                "cf": beneficiario,
                "data": datetime.datetime.now().strftime("%d/%m/%Y"),
                "hash": "LOGICA_PROGRAMMATA",
                "tipo": "Smart Contract",
                "stato": "ATTIVO"
            }
            st.session_state.blockchain.append(nuovo_smart)
            st.success("Smart Contract attivato correttamente!")

# --- 5. REGISTRO COMPLETO ---
elif scelta == "Registro Completo":
    st.header("📜 Libro Mastro Immutabile")
    if st.session_state.blockchain:
        df = pd.DataFrame(st.session_state.blockchain)
        st.dataframe(df, use_container_width=True)
    else:
        st.write("Il registro è ancora vuoto.")
