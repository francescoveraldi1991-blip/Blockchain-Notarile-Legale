import streamlit as st
import hashlib
import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Archivio e Verifica - NotaryChain Pro",
    page_icon="📜",
    layout="wide"
)

# 2. DESIGN COORDINATO LUXURY
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        .stApp { background-color: #fdfdfd; }
        [data-testid="stSidebar"] {
            background-color: #0e1621 !important;
            border-right: 3px solid #b89333;
        }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p { color: #ffffff !important; }
        h1, h2, h3, h4, label, p, span {
            font-family: 'Inter', sans-serif !important;
            color: #1a2a6c !important;
        }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
        .notary-card {
            background: white;
            padding: 30px;
            border-radius: 20px;
            border: 1px solid #f1f1f1;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        input { color: #000000 !important; }
        .stTextInput>div>div>input {
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
        }
        /* Pulsanti White & Gold */
        div.stButton > button, .stDownloadButton > button {
            background-color: white !important;
            color: #b89333 !important;
            border: 1px solid #b89333 !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
            font-weight: 600 !important;
        }
        div.stButton > button:hover, .stDownloadButton > button:hover {
            background-color: #b89333 !important;
            color: white !important;
        }
        .hash-text {
            color: #b89333;
            font-family: monospace;
            background: #fff9eb;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.85rem;
            word-break: break-all;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.title("📜 Archivio e Verifica")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Gestisci i tuoi atti e verifica l\'autenticità dei documenti in tempo reale.</p>', unsafe_allow_html=True)

# --- FUNZIONE 2: VERIFICA ORIGINALITÀ ---
st.markdown("### 🛡️ Verifica Integrità Documento")
with st.expander("Clicca qui per verificare se un file PDF in tuo possesso è originale"):
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    file_da_verificare = st.file_uploader("Carica il file da controllare", type=["pdf"], key="verify_upload")
    
    if file_da_verificare:
        bytes_data = file_da_verificare.getvalue()
        hash_check = hashlib.sha256(bytes_data).hexdigest()
        
        # Cerchiamo l'hash nel database
        match = next((x for x in st.session_state.blockchain if x['hash'] == hash_check), None)
        
        if match:
            st.success(f"✅ DOCUMENTO AUTENTICO: Trovata corrispondenza nel registro per l'atto '{match['nome']}' notarizzato il {match['data']}.")
        else:
            st.error("❌ DOCUMENTO NON TROVATO: L'impronta di questo file non risulta nel registro. Il file potrebbe essere stato alterato o mai notarizzato.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- RICERCA ---
st.markdown('<div class="notary-card">', unsafe_allow_html=True)
st.subheader("🔍 Filtri di Ricerca")
col_cf, col_piva = st.columns(2)
with col_cf:
    search_cf = st.text_input("Ricerca per Codice Fiscale").upper()
with col_piva:
    search_piva = st.text_input("Ricerca per Partita IVA")
st.markdown('</div>', unsafe_allow_html=True)

# Logica priorità
query_effettiva = search_cf if search_cf else search_piva

# --- VISUALIZZAZIONE RISULTATI + FUNZIONE 1: DOWNLOAD ---
st.subheader("📑 Atti Registrati")

if not st.session_state.blockchain:
    st.info("Nessun atto registrato nel sistema.")
else:
    atti_filtrati = [atto for atto in st.session_state.blockchain if query_effettiva in atto['identificativo'].upper() or not query_effettiva]

    if atti_filtrati:
        for atto in atti_filtrati:
            with st.container():
                st.markdown(f"""
                <div class="notary-card">
                    <div style="display: flex; justify-content: space-between;">
                        <h3 style='margin:0;'>{atto['nome']}</h3>
                        <span style="color: #b89333; font-weight: bold;">{atto['data']}</span>
                    </div>
                    <p><b>Identificativo:</b> {atto['identificativo']}</p>
                    <div class="hash-text">{atto['hash']}</div>
                """, unsafe_allow_html=True)
                
                # Generazione contenuto del certificato
                cert_content = f"""
                CERTIFICATO DI NOTARIZZAZIONE BLOCKCHAIN
                ---------------------------------------
                Documento: {atto['nome']}
                Data Registrazione: {atto['data']}
                Identificativo Soggetto: {atto['identificativo']}
                Impronta Digitale (SHA-256): {atto['hash']}
                Stato: {atto['stato']}
                
                Validato da NotaryChain Pro.
                """
                
                st.download_button(
                    label="📄 SCARICA CERTIFICATO",
                    data=cert_content,
                    file_name=f"Certificato_{atto['nome']}.txt",
                    mime="text/plain",
                    key=f"btn_{atto['hash']}"
                )
                st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Nessun atto trovato.")

st.sidebar.markdown("---")
st.sidebar.write(f"📊 Atti in Registro: **{len(st.session_state.blockchain)}**")
