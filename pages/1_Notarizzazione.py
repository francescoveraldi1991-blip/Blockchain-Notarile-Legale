import streamlit as st
import hashlib
import datetime

# --- CONFIGURAZIONE E DESIGN (Uguale alla Home) ---
st.set_page_config(page_title="NotaryChain - Contratti", page_icon="⚖️", layout="wide")

def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #2c3e50; }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #1a2a6c; }
        
        /* Box Stile Card Bianca */
        .notary-card {
            background-color: white;
            padding: 25px;
            border-radius: 15px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }

        /* Pulsante Blu/Oro */
        div.stButton > button {
            background-color: #1a2a6c;
            color: white;
            border-radius: 8px;
            width: 100%;
            height: 50px;
            font-weight: 600;
        }
        div.stButton > button:hover {
            background-color: #b89333;
            border: none;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# Recupero dati (per non perderli passando da una pagina all'altra)
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# --- CONTENUTO PAGINA ---
st.title("📄 Notarizzazione Contratti")
st.write("Inserisci i dettagli del contratto per generare l'impronta digitale immutabile.")

# Creiamo una colonna centrale per un look pulito
col_sx, col_cent, col_dx = st.columns([1, 2, 1])

with col_cent:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    
    with st.form("form_contratto", clear_on_submit=True):
        st.subheader("Nuovo Inserimento")
        titolo = st.text_input("Titolo del Contratto / Repertorio")
        cf_contraente = st.text_input("Codice Fiscale Parte Principale").upper()
        file_pdf = st.file_uploader("Carica l'Atto in PDF", type=["pdf"])
        
        st.markdown("---")
        consenso = st.checkbox("Certifico l'integrità del documento e l'identità delle parti.")
        
        submit = st.form_submit_button("SIGILLA NELLA BLOCKCHAIN")
        
        if submit:
            if titolo and cf_contraente and file_pdf and consenso:
                # Calcolo Hash
                file_bytes = file_pdf.getvalue()
                impronta = hashlib.sha256(file_bytes).hexdigest()
                
                # Registrazione
                nuovo_blocco = {
                    "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "nome": titolo,
                    "cf": cf_contraente,
                    "hash": impronta,
                    "tipo": "Contratto",
                    "stato": "✅ Certificato"
                }
                st.session_state.blockchain.append(nuovo_blocco)
                st.success("Contratto Notarizzato con Successo!")
                st.balloons()
            else:
                st.error("Tutti i campi sono obbligatori per la validità legale.")
                
    st.markdown('</div>', unsafe_allow_html=True)

# Menu laterale automatico
st.sidebar.markdown("---")
st.sidebar.image("https://img.icons8.com/ios-filled/50/1a2a6c/law.png")
st.sidebar.write("**NotaryChain Pro** v4.5")
