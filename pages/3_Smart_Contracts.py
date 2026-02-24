import streamlit as st
import datetime

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(
    page_title="Smart Contracts - NotaryChain Pro",
    page_icon="📜",
    layout="wide"
)

# 2. DESIGN COORDINATO LUXURY
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        .stApp { background-color: #fdfdfd; }

        /* SIDEBAR */
        [data-testid="stSidebar"] {
            background-color: #0e1621 !important;
            border-right: 3px solid #b89333;
        }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p { color: #ffffff !important; }

        /* TESTI */
        h1, h2, h3, h4, label, p, span {
            font-family: 'Inter', sans-serif !important;
            color: #1a2a6c !important;
        }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

        /* CARD */
        .notary-card {
            background: white;
            padding: 30px;
            border-radius: 20px;
            border: 1px solid #f1f1f1;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }

        /* INPUT TOTAL WHITE */
        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
            background-color: white !important;
            color: black !important;
            border: 2px solid #b89333 !important;
            border-radius: 10px !important;
        }
        
        /* PULSANTI */
        div.stButton > button {
            background-color: white !important;
            color: #b89333 !important;
            border: 2px solid #b89333 !important;
            border-radius: 12px !important;
            padding: 10px 25px !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #b89333 !important;
            color: white !important;
        }

        /* STATUS BADGE */
        .status-badge {
            background: #fff9eb;
            color: #b89333;
            padding: 5px 15px;
            border-radius: 20px;
            border: 1px solid #b89333;
            font-weight: 600;
            font-size: 0.8rem;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

st.title("📜 Smart Contracts")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Configurazione e monitoraggio di contratti digitali auto-eseguibili.</p>', unsafe_allow_html=True)

st.markdown("---")

# Layout a due colonne: Creazione e Monitoraggio
col_sx, col_dx = st.columns([1, 1.2])

with col_sx:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    st.subheader("🛠️ Nuovo Contratto")
    with st.form("smart_contract_form"):
        st.text_input("Titolo dell'Accordo")
        st.selectbox("Tipo di Condizione", ["Pagamento Ricevuto", "Scadenza Temporale", "Firma Multilaterale"])
        st.text_area("Clausole d'Esecuzione")
        st.markdown("<br>", unsafe_allow_html=True)
        submit = st.form_submit_button("ATTIVA SMART CONTRACT")
        if submit:
            st.success("Contratto caricato nella Sandbox")
    st.markdown('</div>', unsafe_allow_html=True)

with col_dx:
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    st.subheader("📡 Contratti in Esecuzione")
    
    # Esempio di contratto attivo
    st.markdown("""
    <div style="border-bottom: 1px solid #eee; padding-bottom: 15px; margin-bottom: 15px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h4 style="margin:0;">Escrow Immobiliare #992</h4>
            <span class="status-badge">IN ATTESA DI FONDI</span>
        </div>
        <p style="font-size: 0.9rem; color: #666; margin-top: 5px;">
            <b>Condizione:</b> Deposito del 10% presso il wallet notarile.<br>
            <b>Scadenza:</b> 30/11/2026
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("Al momento non ci sono altri smart contract attivi per questo studio.")
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("⚡ **Blockchain Engine:**")
st.sidebar.success("Pronto per l'esecuzione")
