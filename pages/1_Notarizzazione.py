with st.container():
    st.markdown('<div style="background-color: #ffffff; padding: 30px; border-radius: 15px; border: 1px solid #eee; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">', unsafe_allow_html=True)
    # Inserisci qui i tuoi st.text_input o st.file_uploader
    st.markdown('</div>', unsafe_allow_html=True)
import streamlit as st
import hashlib
import datetime

st.set_page_config(page_title="Notarizzazione PDF", layout="centered")

# Recuperiamo il registro dalla sessione principale
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.header("📄 Notarizzazione Documentale")
st.write("Usa questo modulo per dare **data certa** e **integrità** ai tuoi documenti PDF.")

# Utilizzo di un 'form' per stabilizzare la grafica del browser
with st.form("form_notarizzazione", clear_on_submit=True):
    st.subheader("Dati dell'Atto")
    
    nome_atto = st.text_input("Identificativo Atto (es. Repertorio n. / Nome Contratto)")
    cf_soggetto = st.text_input("Codice Fiscale del Soggetto coinvolto").upper()
    
    st.divider()
    
    st.subheader("Caricamento File")
    file_caricato = st.file_uploader("Seleziona il file PDF da sigillare", type=["pdf"])
    
    st.warning("⚠️ Nota legale: Sulla blockchain verrà salvata solo l'impronta (Hash). Il contenuto del PDF rimarrà privato.")
    
    consenso = st.checkbox("Confermo l'avvenuta identificazione del soggetto ai fini AML/GDPR")

    # Tasto di invio che processa tutto in un colpo solo
    submit_button = st.form_submit_button("SIGILLA E REGISTRA")

if submit_button:
    if file_caricato and nome_atto and cf_soggetto and consenso:
        # Calcolo dell'impronta digitale (Hash)
        bytes_data = file_caricato.getvalue()
        impronta = hashlib.sha256(bytes_data).hexdigest()
        
        # Creazione del record
        nuovo_atto = {
            "indice": len(st.session_state.blockchain) + 1,
            "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "cf": cf_soggetto,
            "atto": nome_atto,
            "hash": impronta,
            "stato": "Certificato"
        }
        
        # Aggiunta al registro condiviso
        st.session_state.blockchain.append(nuovo_atto)
        
        st.success(f"✅ Atto '{nome_atto}' registrato con successo!")
        st.info(f"**Impronta Digitale:** {impronta}")
    else:
        st.error("❌ Errore: Assicurati di aver compilato tutti i campi, caricato il PDF e spuntato il consenso legale.")

st.sidebar.success("Modulo Notarizzazione caricato.")
