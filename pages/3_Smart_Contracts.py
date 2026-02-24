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
        .stTextInput input, .stSelectbox div[data-baseweb="select"], .stDateInput input, .stNumberInput input {
            background-color: white !important;
            color: black !important;
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
        }

        /* BADGE STATO DINAMICI */
        .status-active { background: #fff3e0; color: #ef6c00; padding: 4px 12px; border-radius: 15px; font-weight: 600; font-size: 0.8rem; border: 1px solid #ef6c00; }
        .status-completed { background: #e8f5e9; color: #2e7d32; padding: 4px 12px; border-radius: 15px; font-weight: 600; font-size: 0.8rem; border: 1px solid #2e7d32; }

        /* FILE UPLOADER STYLE */
        [data-testid="stFileUploader"] section {
            background-color: #fafafa !important;
            border: 1px dashed #b89333 !important;
            border-radius: 10px !important;
            padding: 10px !important;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# Inizializzazione sessione
if 'smart_contracts' not in st.session_state:
    st.session_state.smart_contracts = []

st.title("⚡ Smart Contracts Manager")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Gestione contratti di manutenzione e servizi con sblocco automatico dei fondi.</p>', unsafe_allow_html=True)

st.markdown("---")

col_setup, col_monitor = st.columns([1, 1.3])

# --- COLONNA SINISTRA: CREAZIONE ---
with col_setup:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    st.subheader("🛠️ Crea Nuovo Accordo")
    
    with st.form("sc_form", clear_on_submit=True):
        nome_contratto = st.text_input("Oggetto del Contratto")
        fornitore = st.text_input("Fornitore (P.IVA)")
        
        c1, c2 = st.columns(2)
        with c1:
            budget = st.number_input("Budget (€)", min_value=0.0, step=50.0)
        with c2:
            scadenza = st.date_input("Scadenza", datetime.date.today() + datetime.timedelta(days=30))
        
        trigger = st.selectbox("Trigger di Sblocco", ["Caricamento Verbale", "Approvazione Cliente"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        attivazione = st.form_submit_button("ATTIVA SMART CONTRACT")
        
        if attivazione and nome_contratto:
            nuovo_sc = {
                "id": hashlib.md5(nome_contratto.encode()).hexdigest()[:8],
                "nome": nome_contratto,
                "fornitore": fornitore,
                "budget": budget,
                "scadenza": scadenza.strftime("%d/%m/%Y"),
                "stato": "IN ATTESA",
                "tipo": trigger,
                "completato": False
            }
            st.session_state.smart_contracts.append(nuovo_sc)
            st.success("Contratto deployato con successo!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLONNA DESTRA: MONITORAGGIO ---
with col_monitor:
    st.subheader("📡 Monitoraggio in Tempo Reale")
    
    if not st.session_state.smart_contracts:
        st.info("Nessun contratto attivo nel sistema.")
    else:
        for idx, sc in enumerate(st.session_state.smart_contracts):
            # Determiniamo la classe CSS del badge
            badge_class = "status-completed" if sc['completato'] else "status-active"
            status_text = "COMPLETATO - PAGAMENTO SBLOCCATO" if sc['completato'] else "IN ATTESA DI VERBALE"
            
            st.markdown(f"""
            <div class="notary-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin:0;">{sc['nome']}</h4>
                    <span class="{badge_class}">{status_text}</span>
                </div>
                <hr style="margin: 10px 0; border: 0; border-top: 1px solid #eee;">
                <p style="font-size: 0.9rem; margin-bottom: 10px;">
                    <b>Partner:</b> {sc['fornitore']} | <b>Importo:</b> €{sc['budget']:,}<br>
                    <b>Scadenza:</b> {sc['scadenza']} | <b>ID:</b> SC-{sc['id']}
                </p>
            """, unsafe_allow_html=True)
            
            # Se il contratto non è completato, mostriamo il caricamento verbale
            if not sc['completato']:
                file_verbale = st.file_uploader(f"Carica Verbale per {sc['nome']}", type=["pdf"], key=f"up_{sc['id']}")
                if file_verbale:
                    # Logica di sblocco
                    st.session_state.smart_contracts[idx]['completato'] = True
                    st.session_state.smart_contracts[idx]['stato'] = "COMPLETATO"
                    st.rerun()
            else:
                st.markdown("<p style='color: #2e7d32; font-weight: bold;'>✅ Fondi trasferiti con successo al fornitore.</p>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("⚡ **Smart Engine:** Attivo")
st.sidebar.write(f"Contratti gestiti: **{len(st.session_state.blockchain) + len(st.session_state.smart_contracts)}**")
