import streamlit as st

def apply_custom_design():
    st.markdown("""
        <style>
        /* Sfondo generale e font */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #2c3e50;
        }

        /* Titoli eleganti */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #1a2a6c; /* Blu Notte */
        }

        /* Navbar Laterale */
        [data-testid="stSidebar"] {
            background-color: #f8f9fa;
            border-right: 1px solid #e0e0e0;
        }

        /* Card Effetto Vetro per i contenuti */
        div.stButton > button {
            background-color: #1a2a6c;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 24px;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        
        div.stButton > button:hover {
            background-color: #b89333; /* Oro */
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transform: translateY(-2px);
        }

        /* Input Campi */
        .stTextInput>div>div>input {
            border-radius: 8px;
        }
        
        /* Box di successo dorati */
        .stSuccess {
            background-color: rgba(184, 147, 51, 0.1);
            color: #b89333;
            border: 1px solid #b89333;
        }
        </style>
    """, unsafe_allow_html=True)

# Applichiamo il design
apply_custom_design()

# --- IL RESTO DEL TUO CODICE HOME ---
# --- PARTE ALTA (Mantieni questa) ---
import streamlit as st

def apply_custom_design():
    # ... (il codice CSS del Passo 1) ...

apply_custom_design()

st.title("⚖️ NotaryChain Pro")
st.markdown("---")

# =========================================================
# QUI SOSTITUISCI: Cancella i vecchi st.write e st.info
# E INCOLLA IL CODICE DEL PASSO 2:
# =========================================================

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Sicurezza. Trasparenza. Futuro.")
    st.write("""
        Benvenuti nell'ecosistema **NotaryChain**. 
        La nostra tecnologia trasforma il concetto di 'Data Certa' in uno standard 
        digitale immutabile, proteggendo la proprietà intellettuale e le 
        volontà testamentarie con crittografia di grado militare.
    """)
    st.button("Esplora l'Archivio")

with col2:
    st.markdown("![Legal Icon](https://img.icons8.com/ios-filled/150/1a2a6c/law.png)")

# =========================================================
# FINE SOSTITUZIONE
# =========================================================

st.markdown("---")

# --- PARTE BASSA (Mantieni questa per non perdere i dati) ---
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []
# Inizializziamo il registro una sola volta per tutte le pagine
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []
