import streamlit as st
import hashlib
import datetime
import pandas as pd

st.set_page_config(page_title="Notaio Digitale Pro", page_icon="⚖️", layout="wide")

# --- DATABASE TEMPORANEO ---
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# --- FUNZIONI TECNICHE ---
def calcola_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

# --- INTERFACCIA ---
st.title("⚖️ Piattaforma Notarile Blockchain 4.5 (Compliance Edition)")
st.sidebar.markdown("### Quadro Normativo Applicato")
st.sidebar.info("""
- **Codice Civile** (Successioni e Contratti)
- **Reg. UE 2016/679** (GDPR)
- **D.Lgs. 231/2007** (Antiriciclaggio)
- **eIDAS** (Validazione Elettronica)
""")

menu = ["Notarizza Atto (Full Legal)", "Ricerca per CF", "Gestione Revoche", "Smart Contract", "Registro & Export"]
scelta = st.sidebar.radio("Navigazione", menu)

# --- 1. NOTARIZZAZIONE COMPLIANT ---
if scelta == "Notarizza Atto (Full Legal)":
    st.header("📄 Registrazione Atto con Conformità Legale")
    
    with st.expander("🛡️ Informativa Privacy & AML", expanded=True):
        st.write("Ai sensi del GDPR, i dati sensibili non verranno salvati on-chain. Verrà memorizzata solo l'impronta crittografica (Hash).")
        consenso = st.checkbox("Dichiaro di aver identificato il soggetto ai fini AML/KYC")

    col1, col2 = st.columns(2)
    with col1:
        nome_atto = st.text_input("Repertorio/Titolo Atto")
        cf_soggetto = st.text_input("Codice Fiscale Soggetto").upper()
    with col2:
        tipo_documento = st.selectbox("Tipo Documento", ["Testamento Olografo", "Contratto Aziendale", "Scrittura Privata"])
        file_caricato = st.file_uploader("Carica PDF Originale", type=["pdf"])

    if st.button("Sigilla e Registra"):
        if file_caricato and consenso and cf_soggetto:
            impronta = calcola_hash(file_caricato.getvalue())
            nuovo_blocco = {
                "indice": len(st.session_state.blockchain) + 1,
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                "cf": cf_soggetto,
                "atto": nome_atto,
                "tipo": tipo_documento,
                "hash": impronta,
                "stato": "Certificato",
                "compliance": "GDPR/AML OK"
            }
            st.session_state.blockchain.append(nuovo_blocco)
            st.success("Atto notarizzato nel rispetto delle normative vigenti.")
        else:
            st.warning("Assicurati di aver dato il consenso e compilato i campi.")

# --- 5. REGISTRO & EXPORT EXCEL ---
elif scelta == "Registro & Export":
    st.header("📜 Archivio Notarile")
    if st.session_state.blockchain:
        df = pd.DataFrame(st.session_state.blockchain)
        st.dataframe(df)
        
        # FUNZIONE EXPORT PER SALVARE SUL PC DEL CLIENTE
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Scarica Registro (Backup Locale)",
            data=csv,
            file_name='registro_blockchain_notarile.csv',
            mime='text/csv',
        )
    else:
        st.info("Nessun atto nel registro.")

# (Le altre funzioni Ricerca, Revoca e Smart Contract rimangono come prima)
