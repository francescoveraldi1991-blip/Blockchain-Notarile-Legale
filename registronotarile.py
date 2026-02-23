import streamlit as st

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="NotaryChain Pro - Home",
    page_icon="⚖️",
    layout="wide"
)

# 2. DESIGN POTENZIATO (ALTO CONTRASTO E COLORI COORDINATI)
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        /* --- SFONDO E CORPO --- */
        .stApp {
            background-color: #ffffff;
        }

        /* --- SIDEBAR SCURA PROFESSIONALE --- */
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

        /* --- TITOLI E TESTO INTRODUTTIVO (BLU NOTARY) --- */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #1a2a6c !important;
        }

        /* Testo di benvenuto personalizzato in Blu */
        .testo-introduzione {
            font-family: 'Inter', sans-serif;
            color: #1a2a6c !important;
            font-size: 1.25rem;
            line-height: 1.6;
            font-weight: 400;
        }

        /* --- PULSANTE LUXURY --- */
        div.stButton > button {
            background: linear-gradient(135deg, #1a2a6c 0%, #b89333 100%);
            color: white !important;
            border-radius: 12px;
            border: none;
            padding: 15px 30px;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        div.stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(184, 147, 51, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# 3. INIZIALIZZAZIONE BLOCKCHAIN
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# 4. LAYOUT CONTENUTI
st.title("⚖️ NotaryChain Pro")
st.markdown("---")

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("## Sicurezza. Trasparenza. Futuro.")
    
    # --- TESTO IN BLU ---
    st.markdown("""
        <p class="testo-introduzione">
            Benvenuti nell'ecosistema <b>NotaryChain</b>. <br>
            La nostra tecnologia trasforma il concetto di 'Data Certa' in uno standard 
            digitale immutabile, proteggendo la proprietà intellettuale e le 
            volontà testamentarie con crittografia di grado militare.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- IL COLLEGAMENTO CHE HAI CHIESTO ---
    if st.button("ENTRA NELLA BLOCKCHAIN LEGALE"):
        st.switch_page("pages/1_Notarizzazione.py")

with col2:
    # Immagine istituzionale
    st.markdown("![Legal Icon](https://img.icons8.com/ios-filled/150/1a2a6c/law.png)")

st.markdown("---")
st.info("💡 Suggerimento: Usa il menu a sinistra per navigare rapidamente tra i moduli di ricerca e gestione.")
