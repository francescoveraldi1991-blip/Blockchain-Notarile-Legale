import streamlit as st
import hashlib

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Archivio e Verifica - NotaryChain Pro",
    page_icon="📜",
    layout="wide"
)

# 2. DESIGN COORDINATO LUXURY (Mantenuto identico)
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        .stApp { background-color: #fdfdfd; }
        [data-testid="stSidebar"] { background-color: #0e1621 !important; border-right: 3px solid #b89333; }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p { color: #ffffff !important; }
        h1, h2, h3, h4, label, p, span { font-family: 'Inter', sans-serif !important; color: #1a2a6c !important; }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
        .notary-card { background: white; padding: 30px; border-radius: 20px; border: 2px solid #b89333; box-shadow: 0 15px 35px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .stTextInput input { background-color: white !important; color: black !important; border: 2px solid #b89333 !important; border-radius: 10px !important; }
        [data-testid="stFileUploader"] section { background-color: white !important; border: 2px dashed #b89333 !important; border-radius: 12px !important; }
        div.stButton > button, .stDownloadButton > button { background-color: white !important; color: #b89333 !important; border: 2px solid #b89333 !important; border-radius: 8px !important; font-weight: 600 !important; }
        div.stButton > button:hover, .stDownloadButton > button:hover { background-color: #b89333 !important; color: white !important; }
        .hash-text { color: #b89333; font-family: monospace; background: #fff9eb; padding: 8px 12px; border-radius: 8px; font-size: 0.85rem; word-break: break-all; margin-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.title("📜 Archivio e Verifica")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Gestione e download dei certificati notarili ufficiali.</p>', unsafe_allow_html=True)

# --- VERIFICA --- (Codice invariato)
with st.expander("🛡️ Verifica Integrità Documento"):
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    file_da_verificare = st.file_uploader("", type=["pdf"], key="verify_upload", label_visibility="collapsed")
    if file_da_verificare:
        hash_check = hashlib.sha256(file_da_verificare.getvalue()).hexdigest()
        match = next((x for x in st.session_state.blockchain if x['hash'] == hash_check), None)
        if match: st.success(f"✅ DOCUMENTO AUTENTICO: '{match['nome']}'")
        else: st.error("❌ DOCUMENTO NON TROVATO")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- RICERCA --- (Codice invariato)
st.markdown('<div class="notary-card">', unsafe_allow_html=True)
st.subheader("🔍 Filtri di Ricerca")
c1, c2 = st.columns(2)
with c1: search_cf = st.text_input("Codice Fiscale", key="search_cf_arch").upper()
with c2: search_piva = st.text_input("Partita IVA", key="search_piva_arch")
st.markdown('</div>', unsafe_allow_html=True)

query = search_cf if search_cf else search_piva

# --- RISULTATI E GENERAZIONE CERTIFICATO ACCATTIVANTE ---
st.subheader("📑 Atti Registrati")

if not st.session_state.blockchain:
    st.info("Nessun atto registrato.")
else:
    atti_filtrati = [a for a in st.session_state.blockchain if query in a['identificativo'].upper() or not query]

    for i, atto in enumerate(atti_filtrati):
        with st.container():
            st.markdown(f"""
            <div class="notary-card">
                <div style="display: flex; justify-content: space-between;">
                    <h3 style='margin:0;'>{atto['nome']}</h3>
                    <span style="color: #b89333; font-weight: bold;">{atto['data']}</span>
                </div>
                <p style="margin-bottom:5px;"><b>ID Soggetto:</b> {atto['identificativo']} | <b>Luogo:</b> {atto.get('luogo', 'Milano')}</p>
                <div class="hash-text">{atto['hash']}</div>
            """, unsafe_allow_html=True)
            
            # --- CREAZIONE CONTENUTO CERTIFICATO HTML (GRAFICA ACCATTIVANTE) ---
            luogo = atto.get('luogo', 'Milano')
            html_cert = f"""
            <div style="font-family: 'serif'; padding: 50px; border: 15px solid #b89333; background: white; color: #0e1621; text-align: center;">
                <h1 style="color: #b89333; font-size: 32px;">NOTARYCHAIN PRO</h1>
                <h2 style="text-transform: uppercase; letter-spacing: 2px;">Certificato di Notarizzazione Digitale</h2>
                <hr style="border: 1px solid #b89333; width: 50%;">
                <div style="text-align: left; margin-top: 40px; line-height: 1.6;">
                    <p><b>TITOLO ATTO:</b> {atto['nome']}</p>
                    <p><b>IDENTIFICATIVO SOGGETTO:</b> {atto['identificativo']}</p>
                    <p><b>DATA DI REGISTRAZIONE:</b> {atto['data']}</p>
                    <p><b>LUOGO DI CONCLUSIONE:</b> {luogo}</p>
                    <p><b>IMPRONTA DIGITALE (HASH SHA-256):</b><br><span style="font-family: monospace; font-size: 12px;">{atto['hash']}</span></p>
                    <br>
                    <div style="border-top: 1px solid #eee; padding-top: 20px; font-style: italic;">
                        <p>Il sottoscritto compilatore conferma di aver accertato l'identità personale delle parti e, 
                        in caso di società, i relativi poteri di rappresentanza tramite verifica documentale.</p>
                        <p>Si conferma che l'utente ha apposto la propria firma autografa digitale a corredo della presente dichiarazione, 
                        sigillando il fascicolo in modo immutabile nella rete NotaryChain.</p>
                    </div>
                </div>
                <div style="margin-top: 50px;">
                    <p style="font-size: 10px; color: #999;">Generato elettronicamente tramite Protocollo Blockchain NotaryChain Pro</p>
                </div>
            </div>
            """
            
            c_vuota, c_btn1, c_btn2 = st.columns([2.5, 0.8, 0.7])
            with c_btn1:
                # Per scaricare in formato HTML (che è visualizzabile come PDF/Stampa da ogni browser)
                st.download_button(
                    "📄 SCARICA PDF", 
                    html_cert, 
                    file_name=f"Certificato_{atto['nome']}.html", 
                    mime="text/html",
                    key=f"dl_{i}"
                )
            with c_btn2:
                if st.button("🗑️ ELIMINA", key=f"del_{i}"):
                    st.session_state.blockchain = [x for x in st.session_state.blockchain if x['hash'] != atto['hash']]
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
