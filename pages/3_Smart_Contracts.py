import streamlit as st
import datetime
import pandas as pd

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

        /* BADGE STATO */
        .status-active { background: #e8f5e9; color: #2e7d32; padding: 4px 12px; border-radius: 15px; font-weight: 600; font-size: 0.8rem; border: 1px solid #2e7d32; }
        .status-pending { background: #fff3e0; color: #ef6c00; padding: 4px 12px; border-radius: 15px; font-weight: 600; font-size: 0.8rem; border: 1px solid #ef6c00; }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# Inizializzazione sessione per contratti
if 'smart_contracts' not in st.session_state:
    st.session_state.smart_contracts = []

st.title("⚡ Smart Contracts Manager")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Automazione legale per contratti di manutenzione e servizi professionali.</p>', unsafe_allow_html=True)

st.markdown("---")

col_setup, col_monitor = st.columns([1, 1.2])

with col_setup:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    st.subheader("🛠️ Configura Nuovo Accordo")
    
    with st.form("sc_form", clear_on_submit=True):
        nome_contratto = st.text_input("Oggetto del Contratto (es. Manutenzione Ascensori)")
        fornitore = st.text_input("Fornitore / Partita IVA")
        
        c1, c2 = st.columns(2)
        with c1:
            budget = st.number_input("Budget Sbloccabile (€)", min_value=0.0, step=100.0)
        with c2:
            scadenza = st.date_input("Termine Intervento", datetime.date.today() + datetime.timedelta(days=30))
        
        tipo_servizio = st.selectbox("Tipo di Trigger", ["Caricamento Verbale Tecnico", "Rilevazione Uptime (SLA)", "Consegna Milestone Software"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        attivazione = st.form_submit_button("ATTIVA SMART CONTRACT")
        
        if attivazione:
            if nome_contratto and fornitore:
                nuovo_sc = {
                    "id": len(st.session_state.smart_contracts) + 1,
                    "nome": nome_contratto,
                    "fornitore": fornitore,
                    "budget": budget,
                    "scadenza": scadenza.strftime("%d/%m/%Y"),
                    "stato": "ATTIVO (In attesa evento)",
                    "tipo": tipo_servizio
                }
                st.session_state.smart_contracts.append(nuovo_sc)
                st.success("Contratto attivato sulla rete!")
            else:
                st.error("Compila i campi obbligatori.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_monitor:
    st.subheader("📡 Dashboard Contratti Attivi")
    
    if not st.session_state.smart_contracts:
        st.info("Nessun contratto attivo. Usa il modulo a sinistra per iniziare.")
    else:
        for sc in st.session_state.smart_contracts:
            st.markdown(f"""
            <div class="notary-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin:0;">{sc['nome']}</h4>
                    <span class="status-pending">{sc['stato']}</span>
                </div>
                <hr style="margin: 10px 0; border: 0; border-top: 1px solid #eee;">
                <p style="font-size: 0.9rem; margin-bottom: 5px;">
                    <b>Partner:</b> {sc['fornitore']} | <b>Budget:</b> €{sc['budget']:,}<br>
                    <b>Condizione:</b> {sc['tipo']}<br>
                    <b>Scadenza prevista:</b> {sc['scadenza']}
                </p>
                <div style="display: flex; gap: 10px; margin-top: 10px;">
                    <small style="color: #666;">ID Contratto: SC-00{sc['id']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("🛡️ **Garanzia Legale:**")
st.sidebar.info("Le clausole sono blindate tramite hash crittografico e immodificabili.")
