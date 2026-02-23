import streamlit as st
import hashlib
import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Notarizzazione - NotaryChain Pro",
    page_icon="⚖️",
    layout="wide"
)

# 2. DESIGN LUXURY
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        .stApp { background-color: #fdfdfd; }
        [data-testid="stSidebar"] {
            background-color: #0e1621 !important;
            border-right: 3px solid #b89333;
        }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p { color: #ffffff !important; }
        h1, h2, h3, h4, label, p, span {
            font-family: 'Inter', sans-serif !important;
            color: #1a2a6c !important;
        }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
        [data-testid="stForm"], .stForm { border: none !important; padding: 0 !important; box-shadow: none !important; }
        .notary-card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            border: 1px solid #f1f1f1;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        }
        input { color: #000000 !important; }
        .stTextInput>div>div>input {
            background-color: white !important;
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
            color: #000000 !important;
        }
        [data-testid="stFileUploader"] section {
            background-color: white !important;
            border: 2px dashed #b89333 !important;
            border-radius: 12px !important;
        }
        [data-testid="stFileUploader"] button {
            background-color: white !important;
            color: #b89333 !important;
            border: 1px solid #b89333 !important;
            border-radius: 8px !important;
        }
        div.stButton > button {
            background-color: white !important;
            color: #b89333 !important;
            border: 2px solid #b89333 !important;
            border-radius: 12px !important;
            padding: 15px 30px !important;
            font-weight: 600 !important;
            width: 100% !important;
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

# 4. CONTENUTO
st.title("📄 Notarizzazione Digitale")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Registra l\'impronta digitale dell\'atto selezionando i criteri di verifica corretti.</p>', unsafe_allow_html=True)
st.markdown("---")

col_sx, col_main, col_dx = st.columns([1, 2, 1])

with col_main:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    
    with st.form("form_notarizzazione", clear_on_submit=True):
        st.subheader("📝 Dettagli del Documento")
        titolo_atto = st.text_input("Titolo dell'Atto / Identificativo")
        
        c1, c2 = st.columns(2)
        with c1:
            cf_contraente = st.text_input("Codice Fiscale").upper()
        with c2:
            piva_contraente = st.text_input("Partita IVA")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📂 Caricamento Documento")
        file_pdf = st.file_uploader("Carica il PDF", type=["pdf"], label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("⚖️ Dichiarazioni di Responsabilità")
        
        check_integrita = st.checkbox("Confermo l'integrità e la paternità del documento.")
        check_identita = st.checkbox("Mi sono accertato dell'identità personale delle parti (Obbligatorio per CF).")
        check_poteri = st.checkbox("Ho verificato i relativi poteri di rappresentanza (Obbligatorio per P.IVA).")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submit = st.form_submit_button("SIGILLA ATTO NELLA BLOCKCHAIN")
        
        if submit:
            # Errori di base
            if not titolo_atto:
                st.error("Inserire il titolo dell'atto.")
            elif not file_pdf:
                st.error("Caricare il file PDF.")
            elif not (cf_contraente or piva_contraente):
                st.error("Inserire almeno uno tra Codice Fiscale o Partita IVA.")
            elif not check_integrita:
                st.error("È obbligatorio confermare l'integrità del documento.")
            else:
                # LOGICA CONDIZIONALE RICHIESTA
                valido = True
                messaggio_errore = ""

                # Se c'è il CF, serve l'Identità
                if cf_contraente and not check_identita:
                    valido = False
                    messaggio_errore = "Per procedere con il Codice Fiscale è necessaria la verifica dell'Identità Personale."
                
                # Se c'è la P.IVA, servono i Poteri
                if piva_contraente and not check_poteri:
                    valido = False
                    messaggio_errore = "Per procedere con la Partita IVA è necessaria la verifica dei Poteri di Rappresentanza."

                if valido:
                    file_bytes = file_pdf.getvalue()
                    impronta_hash = hashlib.sha256(file_bytes).hexdigest()
                    
                    nuovo_atto = {
                        "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                        "nome": titolo_atto, 
                        "identificativo": cf_contraente if cf_contraente else piva_contraente,
                        "hash": impronta_hash, 
                        "stato": "✅ Certificato"
                    }
                    st.session_state.blockchain.append(nuovo_atto)
                    st.success("✅ Atto registrato con successo!")
                    st.balloons()
                else:
                    st.error(f"⚠️ {messaggio_errore}")
                
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("🔒 **Sicurezza:**")
st.sidebar.success("Blockchain Core Attiva")
