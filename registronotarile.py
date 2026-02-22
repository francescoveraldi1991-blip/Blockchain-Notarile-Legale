import streamlit as st

# 1. DEFINIZIONE DELLA FUNZIONE (Tutto quello che è "dentro" è spostato a destra)
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #2c3e50;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #1a2a6c;
        }

        [data-testid="stSidebar"] {
            background-color: #f8f9fa;
            border-right: 1px solid #e0e0e0;
        }

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
            background-color: #b89333;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transform: translateY(-2px);
        }
        </style>
    """, unsafe_allow_html=True)

# 2. CHIAMATA DELLA FUNZIONE (Questa riga torna a inizio riga, senza spazi)
apply_custom_design()

# 3. CONTENUTO DELLA PAGINA
st.title("⚖️ NotaryChain Pro")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Sicurezza. Trasparenza. Futuro.")
    st.write("""
        Benvenuti nell'ecosistema **NotaryChain**. 
        La nostra tecnologia trasforma il concetto di 'Data Certa' in uno standard 
        digitale immutabile, proteggendo la proprietà intellettuale e le 
        volontà testamentarie con crittografia di grado militare.
    """)
    st.button("Entra nella blockchain legale")

with col2:
    st.markdown("![Legal Icon](https://img.icons8.com/ios-filled/150/1a2a6c/law.png)")

st.markdown("---")

# 4. INIZIALIZZAZIONE BLOCKCHAIN (Fondamentale a fine pagina)
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []
