import streamlit as st
import hashlib
import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Notarizzazione - NotaryChain Pro",
    page_icon="⚖️",
    layout="wide"
)

# 2. DESIGN COORDINATO (SIDEBAR SCURA + TESTI BLU)
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        /* --- SFONDO E CORPO --- */
        .stApp {
            background-color: #fdfdfd;
        }

        /* --- SIDEBAR SCURA PROFESSIONALE (Coerente con Home) --- */
        [data-testid="stSidebar"] {
            background-color: #0e1621 !important;
            border-right: 3px solid #b89333;
        }

        /* --- TESTI SIDEBAR --- */
        section[data-testid="stSidebar"] span, 
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] label {
            color: #ffffff !important;
            font-size: 1.1rem !important;
        }

        /* --- TITOLI E TESTI (BLU NOTARY) --- */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #1a2a6c !important;
        }
        
        .testo-istruzioni {
            color: #1a2a6c !important;
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
        }

        /* --- CARD CENTRALE PER IL FORM --- */
        .notary-card {
            background: white;
            padding: 35px;
            border-radius: 20px;
            border: 1px solid #eee;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            margin-top: 20px;
        }

        /* --- PULSANTE LUXURY --- */
        div.stButton > button {
            background: linear-gradient(135deg, #1a2a6c 0%, #b89333 100%);
            color: white !important;
            border-radius: 12px;
            border: none;
            padding: 12px 30px;
            font-weight: 600;
            width: 100%;
        }
        
        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(184, 147, 51, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# 3. RECUPERO DATI BLOCKCHAIN
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# 4. CONTENUTO PAGINA
st.title("📄 Notarizzazione Digitale")
st.markdown("""
    <p class="testo-istruzioni">
        Inserisci i dati del contratto e carica il file originale. 
        Il sistema genererà un <b>Hash SHA-256</b> univoco per garantire l'immutabilità nel tempo.
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# Layout centrato per il modulo
col_sx, col_main, col_dx = st.columns([1, 2, 1])

with col_main:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    
    with st.form("form_notarizzazione", clear_on_submit=True):
        st.subheader("📝 Dettagli del Documento")
        
        titolo_atto = st.text_input("Titolo dell'Atto / Identificativo")
        cf_contraente = st.text_input("Codice Fiscale Parte Principale").upper()
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📂 File da Certificare")
        file_pdf = st.file_uploader("Trascina qui il file PDF dell'atto", type=["pdf"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        certificazione = st.checkbox("Confermo che il file caricato è la versione definitiva dell'atto.")
        
        submit = st.form_submit_button("SIGILLA ATTO NELLA BLOCKCHAIN")
        
        if submit:
            if titolo_atto and cf_contraente and file_pdf and certificazione:
                # Logica Crittografica
                file_bytes = file_pdf.getvalue()
                impronta_hash = hashlib.sha256(file_bytes).hexdigest()
                
                # Creazione Blocco
                nuovo_atto = {
                    "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "nome": titolo_atto,
                    "cf": cf_contraente,
                    "hash": impronta_hash,
                    "stato": "✅ Certificato"
                }
                
                # Salvataggio
                st.session_state.blockchain.append(nuovo_atto)
                st.success("Operazione Completata! L'impronta digitale è stata registrata.")
                st.balloons()
            else:
                st.error("Per favore, compila tutti i campi e accetta la conferma.")
                
    st.markdown('</div>', unsafe_allow_html=True)

# 5. FOOTER SIDEBAR
st.sidebar.markdown("---")
st.sidebar.write("🔒 **Stato Connessione:**")
st.sidebar.success("Blockchain Core Attiva")
