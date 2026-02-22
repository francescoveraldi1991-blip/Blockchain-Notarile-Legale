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
st.title("⚖️ NotaryChain Pro")
st.markdown("---")
st.write("### L'eccellenza della Blockchain al servizio della Legge.")
import streamlit as st

st.set_page_config(page_title="Studio Notarile Digitale", layout="centered")

st.title("⚖️ Benvenuti nello Studio Notarile Blockchain")
st.write("Questo sistema modulare garantisce la massima stabilità e conformità legale.")
st.info("Usa il menu a sinistra per navigare tra le diverse sezioni del software.")

# Inizializziamo il registro una sola volta per tutte le pagine
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []
