import streamlit as st

# Configurazione della pagina (deve essere la prima istruzione)
st.set_page_config(
    page_title="Studio Notarile Digitale - Home",
    page_icon="⚖️",
    layout="centered"
)

# Messaggio di Benvenuto e Presentazione
st.title("⚖️ Benvenuti nello Studio Notarile Digitale")
st.subheader("Piattaforma Blockchain per la Certezza del Diritto")

st.markdown("""
Questa piattaforma modulare è stata progettata per offrire servizi di **Notarizzazione**, 
**Archivio Storico** e **Smart Contracts**, garantendo la massima stabilità e conformità legale.

### 🚀 Navigazione Rapida
Usa il menu a sinistra per accedere ai moduli:
1. **Notarizzazione:** Per sigillare PDF con data certa.
2. **Ricerca:** Per consultare l'archivio tramite Codice Fiscale.
3. **Smart Contracts:** Per programmare accordi auto-esecutivi.

---
**Conformità Legale:**
Il sistema opera nel rispetto del *Decreto Semplificazioni (Art. 8-ter)*, del *GDPR* e delle norme del *Codice Civile*.
""")

# INIZIALIZZAZIONE DELLA BLOCKCHAIN
# Questo pezzetto è fondamentale: tiene vivi i dati tra una pagina e l'altra
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []
    st.toast("Registro Blockchain Inizializzato")

st.info("Seleziona un modulo dal menu a sinistra per iniziare.")
