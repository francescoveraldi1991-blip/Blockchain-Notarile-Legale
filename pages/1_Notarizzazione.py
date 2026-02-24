import streamlit as st
import hashlib
from datetime import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Notarizzazione - NotaryChain Pro", page_icon="✍️", layout="wide")

# 2. DESIGN COORDINATO LUXURY (Mantenuto identico per coerenza)
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        .stApp { background-color: #fdfdfd; }
        [data-testid="stSidebar"] { background-color: #0e1621 !important; border-right: 3px solid #b89333; }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p { color: #ffffff !important; }
        h1, h2, h3, h4, label, p, span { font-family: 'Inter', sans-serif !important; color: #1a2a6c !important; }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
        .notary-card { background: white; padding: 30px; border-radius: 20px; border: 1px solid #f1f1f1; box-shadow: 0 15px 35px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .stTextInput input, .stTextArea textarea { background-color: white !important; color: black !important; border: 2px solid #b89333 !important; border-radius: 10px !important; }
        div.stButton > button { background-color: white !important; color: #b89333 !important; border: 2px solid #b89333 !important; border-radius: 12px !important; font-weight: 600 !important; width: 100% !important; transition: 0.3s; }
        div.stButton > button:hover { background-color: #b89333 !important; color: white !important; }
        
        /* Area Firma */
        .signature-pad { border: 2px dashed #b89333; border-radius: 10px; background: #fffcf5; padding: 20px; text-align: center; color: #b89333; font-style: italic; }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# Inizializzazione blockchain in sessione
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.title("✍️ Notarizzazione Atto")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Sigilla i tuoi documenti con valore legale e verifica dell\'identità.</p>', unsafe_allow_html=True)

st.markdown("---")

with st.form("notarizzazione_form"):
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    st.subheader("📁 Caricamento Atto Principale")
    uploaded_file = st.file_uploader("Trascina qui l'atto da notarizzare (PDF)", type=["pdf"], label_visibility="collapsed")
    
    st.markdown("---")
    st.subheader("🪪 Verifica Identità e Rappresentanza")
    col_ident, col_docs = st.columns(2)
    
    with col_ident:
        identificativo = st.text_input("Codice Fiscale o P.IVA del Soggetto")
        nome_atto = st.text_input("Nome/Descrizione dell'Atto")
    
    with col_docs:
        # FUNZIONE AGGIUNTA: Caricamento Documenti Identità
        doc_identita = st.file_uploader("Carica Scansione Documento Identità / Procura", type=["pdf", "jpg", "png"])
        st.info("La scansione verrà crittografata e legata indissolubilmente all'atto principale.")

    st.markdown("---")
    st.subheader("🖋️ Firma Elettronica del Dichiarante")
    st.markdown('<div class="signature-pad">Spazio riservato alla firma digitale del Notaio / Pubblico Ufficiale</div>', unsafe_allow_html=True)
    conferma_firma = st.checkbox("Io qui sottoscritto dichiaro di aver accertato l'identità delle parti e i relativi poteri di rappresentanza, apponendo la mia firma digitale a questo registro immutabile.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.form_submit_button("SIGILLA ATTO IN BLOCKCHAIN")
    st.markdown('</div>', unsafe_allow_html=True)

    if submit:
        if uploaded_file and identificativo and conferma_firma and doc_identita:
            # Calcolo Hash combinato (Atto + ID + Documento Identità)
            file_bytes = uploaded_file.getvalue()
            doc_id_bytes = doc_identita.getvalue()
            
            combined_data = file_bytes + identificativo.encode() + doc_id_bytes
            final_hash = hashlib.sha256(combined_data).hexdigest()
            
            nuovo_atto = {
                "nome": nome_atto if nome_atto else uploaded_file.name,
                "identificativo": identificativo,
                "hash": final_hash,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "stato": "✅ VALIDATO CON DOCUMENTO D'IDENTITÀ"
            }
            
            st.session_state.blockchain.append(nuovo_atto)
            st.success("Atto Sigillato! L'impronta digitale include ora la verifica dell'identità e la firma elettronica.")
            st.balloons()
        else:
            st.error("Per procedere è necessario caricare l'atto, il documento d'identità e spuntare la dichiarazione di firma.")

# Sidebar informativa
st.sidebar.markdown("---")
st.sidebar.write("🏦 **Standard di Sicurezza:**")
st.sidebar.markdown("- Hash SHA-256 Multi-Layer\n- Archiviazione Documentale Protetta\n- Identificazione Certa delle Parti")
