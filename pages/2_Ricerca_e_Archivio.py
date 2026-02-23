import streamlit as st
import hashlib

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Archivio - NotaryChain Pro",
    page_icon="📜",
    layout="wide"
)

# 2. DESIGN COERENTE (WHITE & GOLD)
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
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p {
            color: #ffffff !important;
        }

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

        /* INPUT NERO */
        input { color: #000000 !important; }
        .stTextInput>div>div>input {
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
        }

        /* TABELLE */
        .stDataFrame {
            border: 1px solid #b89333 !important;
            border-radius: 10px !important;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# 3. RECUPERO DATI
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.title("📜 Archivio Notarile")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Consulta i documenti sigillati e verifica la loro integrità originale.</p>', unsafe_allow_html=True)

st.markdown("---")

# Sezione Ricerca
col_filtro, col_vuota = st.columns([1, 2])
with col_filtro:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    search_query = st.text_input("🔍 Cerca per CF o P.IVA").upper()
    st.markdown('</div>', unsafe_allow_html=True)

# Visualizzazione Atti
if not st.session_state.blockchain:
    st.info("L'archivio è attualmente vuoto. Notarizza il tuo primo atto nella pagina precedente.")
else:
    # Filtriamo i dati in base alla ricerca
    atti_filtrati = [
        atto for atto in st.session_state.blockchain 
        if search_query in atto['identificativo'].upper() or not search_query
    ]

    if atti_filtrati:
        for atto in atti_filtrati:
            with st.container():
                st.markdown(f"""
                <div class="notary-card">
                    <h3 style='margin-top:0;'>{atto['nome']}</h3>
                    <p><b>Data:</b> {atto['data']} | <b>Soggetto:</b> {atto['identificativo']}</p>
                    <code style='color: #b89333; font-size: 0.8rem;'>HASH: {atto['hash']}</code>
                    <p style='color: green; font-weight: 600; margin-bottom:0;'>{atto['stato']}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("Nessun atto trovato per i criteri inseriti.")

# Sidebar di stato
st.sidebar.markdown("---")
st.sidebar.write(f"📊 **Statistiche:**")
st.sidebar.write(f"Atti registrati: {len(st.session_state.blockchain)}")
