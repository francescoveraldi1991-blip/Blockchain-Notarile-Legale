import streamlit as st
import hashlib
import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Notarizzazione - NotaryChain Pro",
    page_icon="⚖️",
    layout="wide"
)

# 2. DESIGN COORDINATO LUXURY (PULITO E SENZA DOPPI BORDI)
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

        /* --- RIMOZIONE RETTANGOLO ST.FORM (IL DOPPIO BORDO) --- */
        [data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
        }

        /* --- CARD CENTRALE (L'UNICA CORNICE VISIBILE) --- */
        .notary-card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            border: 1px solid #f1f1f1;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
            margin-top: 10px;
        }

        /* --- INPUT FIELDS: BIANCHI CON BORDO ORO --- */
        .stTextInput>div>div>input, 
        [data-testid="stFileUploader"] section {
            background-color: white !important;
            border: 2px solid #b89333 !important;
            border-radius: 12px !important;
            color: #1a2a6c !important;
        }

        /* --- PULSANTI WHITE & GOLD --- */
        div.stButton > button, [data-testid="stFileUploader"] button {
            background-color: white !important;
            color: #b89333 !important;
            border: 2px solid #b89333 !important;
            border-radius: 12px !important;
            padding: 12px 30px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            width: 100%;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }
        
        div.stButton > button:hover, [data-testid="stFileUploader"] button:hover {
            background-color: #b89333 !important;
            color: white !important;
            box-shadow: 0 4px 15px rgba(184, 147, 51, 0.3) !important;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# 3. LOGICA BLOCKCHAIN
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# 4. CONTENUTO PAGINA
st.title("📄 Notarizzazione Digitale")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Registra l\'impronta digitale dell\'atto nel registro immutabile.</p>', unsafe_allow_html=True)

st.markdown("---")

col_sx, col_main, col_dx = st.columns([1, 2, 1])

with col_main:
    # Questa è la nostra card "vera"
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    
    with st.form("form_notarizzazione", clear_on_submit=True):
        st.subheader("📝 Dettagli del Documento")
        
        titolo_atto = st.text_input("Titolo dell'Atto / Identificativo")
        cf_contraente = st.text_input("Codice Fiscale Parte Principale").upper()
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📂 Caricamento Documento")
        file_pdf = st.file_uploader("Trascina qui il file PDF dell'atto", type=["pdf"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        certificazione = st.checkbox("Confermo l'integrità del documento.")
        
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
