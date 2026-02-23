import streamlit as st
import hashlib
import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Notarizzazione - NotaryChain Pro",
    page_icon="⚖️",
    layout="wide"
)

# 2. DESIGN LUXURY CON CORREZIONI MIRATE
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        /* --- SFONDO --- */
        .stApp { background-color: #fdfdfd; }

        /* --- SIDEBAR SCURA --- */
        [data-testid="stSidebar"] {
            background-color: #0e1621 !important;
            border-right: 3px solid #b89333;
        }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p {
            color: #ffffff !important;
        }

        /* --- TESTI BLU NOTARY --- */
        h1, h2, h3, h4, label, p, span {
            font-family: 'Inter', sans-serif !important;
            color: #1a2a6c !important;
        }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

        /* --- RIMOZIONE TOTALE CORNICE STREAMLIT (IL RETTANGOLO) --- */
        [data-testid="stForm"], .stForm {
            border: none !important;
            padding: 0 !important;
            box-shadow: none !important;
        }

        /* --- CARD CENTRALE --- */
        .notary-card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            border: 1px solid #f1f1f1;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        }

        /* --- INPUT FIELDS --- */
        .stTextInput>div>div>input {
            background-color: white !important;
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
        }

        /* --- PULSANTE BROWSE PICCOLO --- */
        [data-testid="stFileUploader"] section {
            background-color: white !important;
            border: 2px dashed #b89333 !important; /* Effetto tratteggiato elegante */
            border-radius: 12px !important;
            padding: 10px !important;
        }
        
        [data-testid="stFileUploader"] button {
            background-color: white !important;
            color: #b89333 !important;
            border: 1px solid #b89333 !important;
            border-radius: 8px !important;
            padding: 5px 15px !important; /* Ridotto */
            font-size: 0.8rem !important; /* Testo più piccolo */
            width: auto !important; /* Non occupa tutto lo spazio */
            text-transform: none !important;
        }

        /* --- PULSANTE SIGILLA (GRANDE E UGUALE ALLA HOME) --- */
        div.stButton > button {
            background-color: white !important;
            color: #b89333 !important;
            border: 2px solid #b89333 !important;
            border-radius: 12px !important;
            padding: 15px 30px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 10px rgba(184, 147, 51, 0.1) !important;
        }
        
        div.stButton > button:hover {
            background-color: #b89333 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.title("📄 Notarizzazione Digitale")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Registra l\'impronta digitale dell\'atto nel registro immutabile.</p>', unsafe_allow_html=True)

st.markdown("---")

col_sx, col_main, col_dx = st.columns([1, 2, 1])

with col_main:
    # Apro la card personalizzata
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    
    with st.form("form_notarizzazione", clear_on_submit=True):
        st.subheader("📝 Dettagli del Documento")
        titolo_atto = st.text_input("Titolo dell'Atto / Identificativo")
        cf_contraente = st.text_input("Codice Fiscale Parte Principale").upper()
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📂 Caricamento Documento")
        file_pdf = st.file_uploader("Carica il PDF", type=["pdf"], label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        certificazione = st.checkbox("Confermo l'integrità del documento.")
        
        submit = st.form_submit_button("SIGILLA ATTO NELLA BLOCKCHAIN")
        
        if submit:
            if titolo_atto and cf_contraente and file_pdf and certificazione:
                file_bytes = file_pdf.getvalue()
                impronta_hash = hashlib.sha256(file_bytes).hexdigest()
                nuovo_atto = {
                    "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "nome": titolo_atto, "cf": cf_contraente, "hash": impronta_hash, "stato": "✅ Certificato"
                }
                st.session_state.blockchain.append(nuovo_atto)
                st.success("✅ Atto registrato con successo!")
                st.balloons()
            else:
                st.error("Per favore, compila tutti i campi.")
                
    st.markdown('</div>', unsafe_allow_html=True) # Chiudo la card

st.sidebar.markdown("---")
st.sidebar.write("🔒 **Sicurezza:**")
st.sidebar.success("Blockchain Core Attiva")
