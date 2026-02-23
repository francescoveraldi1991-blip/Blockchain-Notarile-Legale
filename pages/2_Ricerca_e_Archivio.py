import streamlit as st
import hashlib

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Archivio - NotaryChain Pro",
    page_icon="📜",
    layout="wide"
)

# 2. DESIGN COORDINATO (WHITE & GOLD)
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

        /* INPUT RICERCA: BIANCO, BORDO ORO, TESTO NERO */
        input { color: #000000 !important; }
        .stTextInput>div>div>input {
            background-color: white !important;
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
            color: #000000 !important;
            font-weight: 500 !important;
        }

        /* STILE PER GLI HASH (ORO) */
        .hash-text {
            color: #b89333;
            font-family: monospace;
            background: #fff9eb;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.85rem;
            word-break: break-all;
            border: 1px solid #eee;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# 3. RECUPERO DATI
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# 4. CONTENUTO PAGINA
st.title("📜 Archivio Notarile")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Consulta il registro e verifica la validità degli atti notarizzati.</p>', unsafe_allow_html=True)

st.markdown("---")

# Sezione Ricerca Doppia
st.markdown('<div class="notary-card">', unsafe_allow_html=True)
st.subheader("🔍 Filtri di Ricerca")
col_cf, col_piva = st.columns(2)

with col_cf:
    search_cf = st.text_input("Ricerca per Codice Fiscale").upper()
with col_piva:
    search_piva = st.text_input("Ricerca per Partita IVA")
st.markdown('</div>', unsafe_allow_html=True)

# 5. LOGICA DI FILTRO ESCLUDENTE
# Se l'utente scrive il CF, usiamo quello. Se è vuoto, usiamo la P.IVA.
query_effettiva = ""
if search_cf:
    query_effettiva = search_cf
elif search_piva:
    query_effettiva = search_piva

# Visualizzazione Risultati
st.subheader("📑 Atti Registrati")

if not st.session_state.blockchain:
    st.info("L'archivio è vuoto. Carica un atto nella pagina di Notarizzazione.")
else:
    # Filtriamo gli atti: se non c'è nessuna query mostriamo tutto, 
    # altrimenti cerchiamo la query nell'identificativo registrato
    atti_filtrati = [
        atto for atto in st.session_state.blockchain 
        if query_effettiva in atto['identificativo'].upper() or not query_effettiva
    ]

    if atti_filtrati:
        for atto in atti_filtrati:
            st.markdown(f"""
            <div class="notary-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style='margin:0; color: #1a2a6c;'>{atto['nome']}</h3>
                    <span style="color: #b89333; font-weight: bold; background: #fcf8ee; padding: 5px 12px; border-radius: 20px; border: 1px solid #b89333;">{atto['data']}</span>
                </div>
                <hr style="margin: 15px 0; border: 0; border-top: 1px dashed #eee;">
                <p style="margin-bottom: 5px;"><b>Identificativo Soggetto:</b> {atto['identificativo']}</p>
                <p style="margin-bottom: 5px;"><b>Certificazione Blockchain (Hash SHA-256):</b></p>
                <div class="hash-text">{atto['hash']}</div>
                <div style="margin-top: 15px; display: flex; align-items: center;">
                    <span style='color: #28a745; font-weight: 600;'>{atto['stato']}</span>
                    <span style="margin-left: 10px; font-size: 0.8rem; color: #666;">(Immutabile a norma di legge)</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning(f"Nessun risultato trovato per i criteri inseriti.")

# Sidebar
st.sidebar.markdown("---")
st.sidebar.write(f"💼 **Stato Registro:**")
st.sidebar.info(f"Totale atti sigillati: {len(st.session_state.blockchain)}")
