import streamlit as st
import hashlib
import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Notarizzazione - NotaryChain Pro",
    page_icon="⚖️",
    layout="wide"
)

# 2. DESIGN COORDINATO, POTENZIATO E SINCRONIZZATO
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        /* --- SFONDO E CORPO --- */
        .stApp { background-color: #fdfdfd; }

        /* --- SIDEBAR SCURA PROFESSIONALE --- */
        [data-testid="stSidebar"] {
            background-color: #0e1621 !important;
            border-right: 3px solid #b89333;
        }
        section[data-testid="stSidebar"] span, 
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] label {
            color: #ffffff !important;
        }

        /* --- TESTI BLU NOTARY --- */
        h1, h2, h3, h4, label, .stMarkdown, p, span {
            font-family: 'Inter', sans-serif !important;
            color: #1a2a6c !important;
        }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

        /* --- INPUT FIELDS & FILE UPLOADER: BIANCHI CON BORDO ORO --- */
        .stTextInput>div>div>input, 
        [data-testid="stFileUploader"] section {
            background-color: white !important;
            border: 2px solid #b89333 !important;
            border-radius: 12px !important;
            color: #1a2a6c !important;
        }

        /* FORZATURA PULSANTE "BROWSE FILES" (Quello che vedevi scuro) */
        [data-testid="stFileUploader"] button {
            background-color: white !important;
            color: #b89333 !important;
            border: 1px solid #b89333 !important;
            font-weight: 600 !important;
        }
        [data-testid="stFileUploader"] button:hover {
            background-color: #fcf8ee !important;
            border-color: #1a2a6c !important;
            color: #1a2a6c !important;
        }

        /* --- CARD CENTRALE --- */
        .notary-card {
            background: white;
            padding: 35px;
            border-radius: 20px;
            border: 1px solid #eee;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            margin-top: 20px;
        }

        /* --- PULSANTE SIGILLA (SINCRONIZZATO AL 100% CON LA HOME) --- */
        div.stButton > button {
            background: linear-gradient(135deg, #1a2a6c 0%, #b89333 100%) !important;
            color: white !important;
            border-radius: 12px !important;
            border: none !important;
            padding: 15px 30px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            width: 100%;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
            transition: all 0.3s ease !important;
            text-transform: none !important;
        }
        
        div.stButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 6px 20px rgba(184, 147, 51, 0.4) !important;
            color: #ffffff !important;
        }

        /* Rimuoviamo eventuali bordi scuri residui di Streamlit */
        div[data-baseweb="input"] {
            border: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# 3. LOGICA BLOCKCHAIN
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# 4. CONTENUTO PAGINA
st.title("📄 Notarizzazione Digitale")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Inserisci i dati dell\'atto e sigillali in modo immutabile.</p>', unsafe_allow_html=True)

st.markdown("---")

col_sx, col_main, col_dx = st.columns([1, 2, 1])

with col_main:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    with st.form("form_notarizzazione", clear_on_submit=True):
        st.subheader("📝 Dettagli del Documento")
        
        titolo_atto = st.text_input("Titolo dell'Atto / Identificativo")
        cf_contraente = st.text_input("Codice Fiscale Parte Principale").upper()
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📂 Caricamento Documento")
        file_pdf = st.file_uploader("Trascina qui il file PDF dell'atto", type=["pdf"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        certificazione = st.checkbox("Confermo l'integrità e la paternità del documento.")
        
        submit = st.form_submit_button("SIGILLA ATTO NELLA BLOCKCHAIN")
        
        if submit:
            if titolo_atto and cf_contraente and file_pdf and certificazione:
                file_bytes = file_pdf.getvalue()
                impronta_hash = hashlib.sha256(file_bytes).hexdigest()
                
                nuovo_atto = {
                    "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "nome": titolo_atto,
                    "cf": cf_contraente,
                    "hash": impronta_hash,
                    "stato": "✅ Certificato"
                }
                st.session_state.blockchain.append(nuovo_atto)
                st.success("✅ Atto registrato con successo!")
                st.balloons()
            else:
                st.error("Per favore, compila tutti i campi prima di procedere.")
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("🔒 **Sicurezza:**")
st.sidebar.success("Blockchain Core Attiva")
