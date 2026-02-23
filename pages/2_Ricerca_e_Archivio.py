import streamlit as st
import hashlib

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Archivio e Verifica - NotaryChain Pro",
    page_icon="📜",
    layout="wide"
)

# 2. DESIGN COORDINATO LUXURY (CORRETTO)
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        .stApp { background-color: #fdfdfd; }

        /* SIDEBAR */
        [data-testid="stSidebar"] {
            background-color: #0e1621 !important;
            border-right: 3px solid #b89333;
        }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p { color: #ffffff !important; }

        /* TESTI */
        h1, h2, h3, h4, label, p, span {
            font-family: 'Inter', sans-serif !important;
            color: #1a2a6c !important;
        }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

        /* CARD */
        .notary-card {
            background: white;
            padding: 30px;
            border-radius: 20px;
            border: 1px solid #f1f1f1;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }

        /* INPUT RICERCA (FORZATI BIANCHI) */
        input { color: #000000 !important; }
        div[data-baseweb="input"] { background-color: white !important; }
        .stTextInput>div>div>input {
            background-color: white !important;
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
            color: #000000 !important;
        }

        /* FILE UPLOADER (BIANCO E ORO) */
        [data-testid="stFileUploader"] section {
            background-color: white !important;
            border: 2px dashed #b89333 !important;
            border-radius: 12px !important;
        }
        [data-testid="stFileUploader"] button {
            background-color: white !important;
            color: #b89333 !important;
            border: 1px solid #b89333 !important;
            font-size: 0.8rem !important;
            overflow: hidden; /* Evita sovrapposizioni */
        }

        /* PULSANTI */
        div.stButton > button, .stDownloadButton > button {
            background-color: white !important;
            color: #b89333 !important;
            border: 1px solid #b89333 !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: 0.3s;
        }
        div.stButton > button:hover, .stDownloadButton > button:hover {
            background-color: #b89333 !important;
            color: white !important;
        }

        /* PULSANTE ELIMINA (ROSSO SOFT) */
        .btn-delete > div > button {
            border: 1px solid #ff4b4b !important;
            color: #ff4b4b !important;
            font-size: 0.7rem !important;
        }
        .btn-delete > div > button:hover {
            background-color: #ff4b4b !important;
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
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Gestione e validazione degli atti notarizzati.</p>', unsafe_allow_html=True)

# --- VERIFICA ORIGINALITÀ ---
with st.expander("🛡️ Verifica Integrità Documento"):
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    file_da_verificare = st.file_uploader("Carica il file da controllare", type=["pdf"], key="verify_upload", label_visibility="collapsed")
    if file_da_verificare:
        hash_check = hashlib.sha256(file_da_verificare.getvalue()).hexdigest()
        match = next((x for x in st.session_state.blockchain if x['hash'] == hash_check), None)
        if match:
            st.success(f"✅ DOCUMENTO AUTENTICO: Corrisponde all'atto '{match['nome']}'.")
        else:
            st.error("❌ DOCUMENTO NON TROVATO: L'impronta non risulta nel registro.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- RICERCA ---
st.markdown('<div class="notary-card">', unsafe_allow_html=True)
st.subheader("🔍 Filtri di Ricerca")
c1, c2 = st.columns(2)
with c1:
    search_cf = st.text_input("Ricerca per Codice Fiscale", key="search_cf").upper()
with c2:
    search_piva = st.text_input("Ricerca per Partita IVA", key="search_piva")
st.markdown('</div>', unsafe_allow_html=True)

query_effettiva = search_cf if search_cf else search_piva

# --- RISULTATI ---
st.subheader("📑 Atti Registrati")

if not st.session_state.blockchain:
    st.info("Nessun atto registrato.")
else:
    # Filtriamo gli atti
    atti_filtrati = [atto for atto in st.session_state.blockchain if query_effettiva in atto['identificativo'].upper() or not query_effettiva]

    for i, atto in enumerate(atti_filtrati):
        st.markdown(f"""
        <div class="notary-card">
            <div style="display: flex; justify-content: space-between;">
                <h3 style='margin:0;'>{atto['nome']}</h3>
                <span style="color: #b89333; font-weight: bold;">{atto['data']}</span>
            </div>
            <p style="margin-bottom:5px;"><b>Identificativo:</b> {atto['identificativo']}</p>
            <div class="hash-text">{atto['hash']}</div>
            <div style="margin-top:15px; display: flex; gap: 10px;">
        """, unsafe_allow_html=True)
        
        # Colonna per i pulsanti
        col_btn1, col_btn2, col_vuota = st.columns([1, 1, 2])
        
        with col_btn1:
            cert_content = f"CERTIFICATO: {atto['nome']}\nData: {atto['data']}\nHash: {atto['hash']}"
            st.download_button("📄 SCARICA", cert_content, file_name=f"Certificato_{i}.txt", key=f"dl_{i}")
        
        with col_btn2:
            st.markdown('<div class="btn-delete">', unsafe_allow_html=True)
            if st.button("🗑️ ELIMINA", key=f"del_{i}"):
                # Logica eliminazione: rimuove l'atto dalla sessione usando l'hash come riferimento
                st.session_state.blockchain = [x for x in st.session_state.blockchain if x['hash'] != atto['hash']]
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write(f"📊 Totale atti: **{len(st.session_state.blockchain)}**")
