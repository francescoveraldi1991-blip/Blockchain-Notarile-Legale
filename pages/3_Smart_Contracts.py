import streamlit as st
import datetime
import hashlib

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Smart Contracts - NotaryChain Pro",
    page_icon="⚡",
    layout="wide"
)

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
            padding: 25px;
            border-radius: 20px;
            border: 1px solid #f1f1f1;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }

        /* INPUT BIANCO BORDO ORO */
        .stTextInput input, .stSelectbox div[data-baseweb="select"], .stDateInput input {
            background-color: white !important;
            color: black !important;
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
        }

        /* BADGE STATO */
        .status-active { background: #fff3e0; color: #ef6c00; padding: 4px 12px; border-radius: 15px; font-weight: 600; font-size: 0.8rem; border: 1px solid #ef6c00; }
        .status-completed { background: #e8f5e9; color: #2e7d32; padding: 4px 12px; border-radius: 15px; font-weight: 600; font-size: 0.8rem; border: 1px solid #2e7d32; }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# Inizializzazione sessione per Smart Contracts
if 'smart_contracts' not in st.session_state:
    st.session_state.smart_contracts = []

st.title("⚡ Smart Contracts")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Configura ed esegui clausole contrattuali digitali auto-eseguibili.</p>', unsafe_allow_html=True)

st.markdown("---")

# --- DEFINIZIONE COLONNE (Risolve il NameError) ---
col_setup, col_monitor = st.columns([1, 1.3])

# --- COLONNA SINISTRA: CREAZIONE ---
with col_setup:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    st.subheader("🛠️ Configura Smart Contract")
    
    with st.form("sc_form", clear_on_submit=True):
        nome_contratto = st.text_input("Oggetto dell'Accordo")
        beneficiario = st.text_input("ID Beneficiario (Wallet/CF)")
        
        tipo_output = st.selectbox("Azione Automatica al Verificarsi", [
            "Emissione Certificato di Conformità (NFT)",
            "Sblocco Accesso Documentazione Protetta",
            "Notifica Immutabile di Adempimento",
            "Validazione Rating Professionale"
        ])
        
        scadenza = st.date_input("Termine Adempimento", datetime.date.today() + datetime.timedelta(days=15))
        
        st.markdown("<br>", unsafe_allow_html=True)
        attivazione = st.form_submit_button("DEPLOYA SU BLOCKCHAIN")
        
        if attivazione and nome_contratto:
            nuovo_sc = {
                "id": hashlib.md5(nome_contratto.encode()).hexdigest()[:6].upper(),
                "nome": nome_contratto,
                "beneficiario": beneficiario,
                "output": tipo_output,
                "scadenza": scadenza.strftime("%d/%m/%Y"),
                "completato": False,
                "tx_hash": None
            }
            st.session_state.smart_contracts.append(nuovo_sc)
            st.success(f"Contratto SC-{nuovo_sc['id']} pubblicato in rete.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLONNA DESTRA: MONITORAGGIO ---
with col_monitor:
    st.subheader("📡 Status Contratti On-Chain")
    
    if not st.session_state.smart_contracts:
        st.info("In attesa di nuovi contratti da monitorare...")
    else:
        for idx, sc in enumerate(st.session_state.smart_contracts):
            badge_class = "status-completed" if sc['completato'] else "status-active"
            status_text = "ESECUTO" if sc['completato'] else "IN ATTESA DI INPUT"
            
            st.markdown(f"""
            <div class="notary-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin:0;">{sc['nome']}</h4>
                    <span class="{badge_class}">{status_text}</span>
                </div>
                <p style="font-size: 0.9rem; margin-top: 10px;">
                    <b>Beneficiario:</b> {sc['beneficiario']}<br>
                    <b>Azione:</b> {sc['output']}<br>
                    <b>Scadenza:</b> {sc['scadenza']}
                </p>
            """, unsafe_allow_html=True)
            
            if not sc['completato']:
                # Input per triggerare lo smart contract
                file_verbale = st.file_uploader(f"Carica prova adempimento (ID: {sc['id']})", type=["pdf"], key=f"file_{sc['id']}")
                if file_verbale:
                    # Genera un hash della transazione per simulare la blockchain reale
                    tx_hash = hashlib.sha256(f"{sc['id']}{datetime.datetime.now()}".encode()).hexdigest()
                    st.session_state.smart_contracts[idx]['completato'] = True
                    st.session_state.smart_contracts[idx]['tx_hash'] = tx_hash
                    st.rerun()
            else:
                st.markdown(f"""
                <div style="background: #e8f5e9; padding: 12px; border-radius: 10px; border: 1px solid #2e7d32; margin-top: 10px;">
                    <p style="margin:0; color: #2e7d32; font-size: 0.85rem; font-family: monospace;">
                        <b>SUCCESS:</b> Condizione soddisfatta.<br>
                        <b>ACTION:</b> {sc['output']} eseguita.<br>
                        <b>TX HASH:</b> {sc['tx_hash'][:32]}...
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("⚡ **Smart Engine:** Attivo")
