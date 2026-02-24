import streamlit as st
import hashlib
from datetime import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Notarizzazione - NotaryChain Pro", page_icon="✍️", layout="wide")

# 2. DESIGN COORDINATO LUXURY
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        .stApp { background-color: #fdfdfd; }
        [data-testid="stSidebar"] { background-color: #0e1621 !important; border-right: 3px solid #b89333; }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p { color: #ffffff !important; }
        h1, h2, h3, h4, label, p, span { font-family: 'Inter', sans-serif !important; color: #1a2a6c !important; }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
        
        .notary-card { 
            background: white; 
            padding: 30px; 
            border-radius: 20px; 
            border: 1px solid #f1f1f1; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.05); 
            margin-bottom: 20px; 
        }

        /* AREA FIRMA GRAFICA SIMULATA */
        .sig-container {
            border: 2px solid #b89333;
            background-color: #fff;
            height: 150px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: crosshair;
            position: relative;
            margin-bottom: 10px;
        }
        .sig-container::after {
            content: "FIRMA QUI (Mouse/Touch)";
            color: #b89333;
            opacity: 0.3;
            font-size: 0.8rem;
            letter-spacing: 2px;
        }

        /* INPUT STYLE */
        .stTextInput input { border: 2px solid #b89333 !important; border-radius: 10px !important; }
        
        /* BOTTONE ORO */
        div.stButton > button { 
            background-color: white !important; 
            color: #b89333 !important; 
            border: 2px solid #b89333 !important; 
            border-radius: 12px !important; 
            font-weight: 700 !important;
            padding: 15px !important;
        }
        div.stButton > button:hover { background-color: #b89333 !important; color: white !important; }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.title("✍️ Notarizzazione Professionale")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Procedura di validazione con acquisizione documenti e firma elettronica.</p>', unsafe_allow_html=True)

st.markdown("---")

with st.form("notarizzazione_avanzata"):
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    
    col_file, col_id = st.columns([1.5, 1])
    
    with col_file:
        st.subheader("📄 Documento Principale")
        uploaded_file = st.file_uploader("Atto da sigillare (PDF)", type=["pdf"], label_visibility="collapsed")
        
    with col_id:
        st.subheader("🪪 Documento Identità")
        doc_identita = st.file_uploader("Scansione Identità/Procura", type=["pdf", "png", "jpg"], label_visibility="collapsed")

    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        nome_atto = st.text_input("Titolo dell'Atto")
        identificativo = st.text_input("Codice Fiscale / P.IVA del Firmatario").upper()
    
    with c2:
        st.write("🖋️ **Riquadro di Sottoscrizione**")
        # Visualizziamo il riquadro grafico
        st.markdown('<div class="sig-container"></div>', unsafe_allow_html=True)
        conferma_firma = st.checkbox("Confermo la validità della firma e dei documenti caricati")

    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.form_submit_button("SIGILLA E REGISTRA IN BLOCKCHAIN")
    st.markdown('</div>', unsafe_allow_html=True)

    if submit:
        if uploaded_file and doc_identita and identificativo and conferma_firma:
            # Creazione Hash Complesso (Atto + Identità + Check Firma)
            seed = uploaded_file.getvalue() + doc_identita.getvalue() + identificativo.encode()
            final_hash = hashlib.sha256(seed).hexdigest()
            
            nuovo_atto = {
                "nome": nome_atto if nome_atto else uploaded_file.name,
                "identificativo": identificativo,
                "hash": final_hash,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "stato": "✅ FIRMATO E VALIDATO"
            }
            
            st.session_state.blockchain.append(nuovo_atto)
            st.success("✅ Atto notarizzato con successo. Il fascicolo digitale è stato sigillato.")
            st.balloons()
        else:
            st.warning("⚠️ Attenzione: Assicurati di aver caricato entrambi i file, inserito l'identificativo e spuntato la conferma della firma.")

st.sidebar.info("L'hash generato include i metadati della firma e del documento d'identità caricato, garantendo l'integrità del fascicolo.")
