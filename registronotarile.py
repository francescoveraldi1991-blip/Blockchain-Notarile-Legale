import streamlit as st

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="NotaryChain Pro - Home",
    page_icon="⚖️",
    layout="wide"
)

# 2. DESIGN POTENZIATO (ALTO CONTRASTO)
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
            background-color: #0e1621 !important; /* Blu Notte Scurissimo */
            border-right: 3px solid #b89333; /* Separatore Oro */
        }

        /* --- TESTI SIDEBAR (Bianco Puro per Leggibilità) --- */
        section[data-testid="stSidebar"] .css-17l243g, 
        section[data-testid="stSidebar"] span, 
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] li {
            color: #ffffff !important;
            font-size: 1.1rem !important;
            font-weight: 500 !important;
        }

        /* --- TITOLI SIDEBAR --- */
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3 {
            color: #b89333 !important;
            padding-bottom: 10px;
        }

        /* --- CORPO CENTRALE --- */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #1c1c1c;
        }
        
        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #1a2a6c !important;
        }

        /* --- PULSANTE LUXURY --- */
        div.stButton > button {
            background: linear-gradient(135deg, #1a2a6c 0%, #b89333 100%);
            color: white !important;
            border-radius: 12px;
            border: none;
            padding: 15px 30px;
            font-weight: 600;
            font-size: 1.1rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }
        
        div.stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(184, 147, 51, 0.4);
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

# Applichiamo lo stile
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
    st.write("""
        Benvenuti nell'ecosistema **NotaryChain**. 
        La nostra tecnologia trasforma il concetto di 'Data Certa' in uno standard 
        digitale immutabile, proteggendo la proprietà intellettuale e le 
        volontà testamentarie con crittografia di grado militare.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PULSANTE DI NAVIGAZIONE ---
    if st.button("ENTRA NELLA BLOCKCHAIN LEGALE"):
        try:
            # Assicurati che il file si chiami 'notarizzazione.py' in 'pages/'
            st.switch_page("pages/notarizzazione.py")
        except:
            st.error("⚠️ Errore: Il file 'notarizzazione.py' non è stato trovato nella cartella 'pages'.")

with col2:
    # Immagine istituzionale
    st.markdown("![Legal Icon](https://img.icons8.com/ios-filled/150/1a2a6c/law.png)")

st.markdown("---")
st.info("💡 Suggerimento: Usa il menu a sinistra per navigare rapidamente tra i moduli di ricerca e gestione.")
