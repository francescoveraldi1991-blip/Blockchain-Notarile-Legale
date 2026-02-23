import streamlit as st
import hashlib

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Archivio - NotaryChain Pro",
    page_icon="📜",
    layout="wide"
)

# 2. DESIGN COERENTE LUXURY (WHITE & GOLD)
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        .stApp { background-color: #fdfdfd; }

        /* SIDEBAR SCURA */
        [data-testid="stSidebar"] {
            background-color: #0e1621 !important;
            border-right: 3px solid #b89333;
        }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p {
            color: #ffffff !important;
        }

        /* TESTI BLU NOTARY */
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

        /* --- INPUT RICERCA: BIANCO, BORDO ORO, TESTO NERO --- */
        input { color: #000000 !important; }
        .stTextInput>div>div>input {
            background-color: white !important;
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
            color: #000000 !important;
            font-weight: 500 !important;
        }
        
        /* Focus effect */
        .stTextInput>div>div>input:focus {
            border-color: #1a2a6c !important;
            box-shadow: 0 0 0 1px #1a2a6c !important;
        }

        /* STILE PER GLI HASH (ORO) */
        .hash-text {
            color: #b89333;
            font-family: monospace;
            background: #fff9eb;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.85rem;
            word-break: break-all;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# 3. RECUPERO DATI DALLA SESSIONE
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# 4. CONTENUTO PAGINA
st.title("📜 Archivio Notarile")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Ricerca i documenti sigillati nel registro immutabile tramite identificativo.</p>', unsafe_allow_html=True)

st.markdown("---")

# Sezione Ricerca
col_filtro, col_vuota = st.columns([1, 2])
with col_filtro:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    st.subheader("🔍 Filtro di Ricerca")
    search_query = st.text_input("Inserisci CF o P.IVA per filtrare").upper()
    st.markdown('</div>', unsafe_allow_html=True)

# Visualizzazione Risultati
st.subheader("📑 Risultati Registro")

if not st.session_state.blockchain:
    st.info("L'archivio è vuoto. Carica un atto nella pagina di Notarizzazione per vederlo apparire qui.")
else:
    # Filtro logico
    atti_filtrati = [
        atto for atto in st.session_state.blockchain 
        if search_query in atto['identificativo'].upper() or not search_query
    ]

    if atti_filtrati:
        for atto in atti_filtrati:
            st.markdown(f"""
            <div class="notary-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style='margin:0; color: #1a2a6c;'>{atto['nome']}</h3>
                    <span style="color: #b89333; font-weight: bold;">{atto['data']}</span>
                </div>
                <hr style="margin: 15px 0; border: 0; border-top: 1px solid #eee;">
                <p><b>Soggetto Registrato:</b> {atto['identificativo']}</p>
                <p><b>Impronta Digitale (Hash SHA-256):</b></p>
                <div class="hash-text">{atto['hash']}</div>
                <p style='color: #28a745; font-weight: 600; margin-top: 15px;'>{atto['stato']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning(f"Nessun atto trovato per: {search_query}")

# Sidebar informativa
st.sidebar.markdown("---")
st.sidebar.write(f"💼 **Gestione Studio:**")
st.sidebar.write(f"Totale atti in blockchain: **{len(st.session_state.blockchain)}**")
