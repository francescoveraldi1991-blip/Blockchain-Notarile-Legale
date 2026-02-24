import streamlit as st
import hashlib
from datetime import datetime
import streamlit.components.v1 as components

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Notarizzazione - NotaryChain Pro", page_icon="✍️", layout="wide")

# 2. DESIGN COORDINATO LUXURY DEFINITIVO
def apply_custom_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
        
        .stApp { background-color: #fdfdfd; }
        [data-testid="stSidebar"] { background-color: #0e1621 !important; border-right: 3px solid #b89333; }
        section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] p { color: #ffffff !important; }
        
        h1, h2, h3, h4, label, p, span { font-family: 'Inter', sans-serif !important; color: #1a2a6c !important; }
        h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
        
        /* CARD BIANCA BORDO ORO */
        .notary-card { 
            background: white; 
            padding: 30px; 
            border-radius: 20px; 
            border: 2px solid #b89333; /* Bordo oro come richiesto */
            box-shadow: 0 15px 35px rgba(0,0,0,0.05); 
            margin-bottom: 20px; 
        }

        /* INPUT BIANCHI BORDO ORO */
        .stTextInput input, .stTextArea textarea, [data-testid="stFileUploader"] section { 
            background-color: white !important; 
            border: 2px solid #b89333 !important; 
            border-radius: 10px !important; 
            color: black !important;
        }
        
        /* BOTTONE ORO */
        div.stButton > button { 
            background-color: white !important; 
            color: #b89333 !important; 
            border: 2px solid #b89333 !important; 
            border-radius: 12px !important; 
            font-weight: 700 !important;
            padding: 15px !important;
            width: 100%;
        }
        div.stButton > button:hover { background-color: #b89333 !important; color: white !important; }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.title("✍️ Notarizzazione Professionale")
st.markdown('<p style="font-size: 1.1rem; color: #1a2a6c;">Validazione con acquisizione documenti, luogo e firma autografa digitale.</p>', unsafe_allow_html=True)

st.markdown("---")

with st.form("notarizzazione_avanzata"):
    st.markdown('<div class="notary-card">', unsafe_allow_html=True)
    
    col_file, col_id = st.columns(2)
    with col_file:
        st.subheader("📄 Atto Principale")
        uploaded_file = st.file_uploader("Carica Atto (PDF)", type=["pdf"], key="main_doc")
    with col_id:
        st.subheader("🪪 Identità")
        doc_identita = st.file_uploader("Carica Scansione ID (PDF/JPG)", type=["pdf", "png", "jpg"], key="id_doc")

    st.markdown("---")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        nome_atto = st.text_input("Titolo dell'Atto")
    with c2:
        identificativo = st.text_input("Codice Fiscale / P.IVA").upper()
    with c3:
        luogo_firma = st.text_input("Luogo (Città)", value="Milano")

    st.markdown("---")
    
    st.subheader("🖋️ Firma Autografa (Usa il mouse nel riquadro bianco)")
    
    # COMPONENTE FIRMA: Riquadro bianco con bordo oro e tratto nero
    canvas_html = """
    <div style="border: 2px solid #b89333; border-radius: 10px; background: white;">
        <canvas id="sig-canvas" width="600" height="150" style="cursor: crosshair; width: 100%;"></canvas>
    </div>
    <script>
        var canvas = document.getElementById("sig-canvas");
        var ctx = canvas.getContext("2d");
        ctx.strokeStyle = "#000000"; ctx.lineWidth = 2;
        var drawing = false;
        canvas.addEventListener("mousedown", function(e) { drawing = true; ctx.beginPath(); ctx.moveTo(e.offsetX, e.offsetY); });
        canvas.addEventListener("mousemove", function(e) { if(drawing) { ctx.lineTo(e.offsetX, e.offsetY); ctx.stroke(); } });
        canvas.addEventListener("mouseup", function() { drawing = false; });
    </script>
    """
    components.html(canvas_html, height=180)

    conferma_firma = st.checkbox("Dichiaro di aver verificato l'identità e verificato nel caso di una società i relativi poteri e appongo la mia firma.")

    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.form_submit_button("SIGILLA ATTO IN BLOCKCHAIN")
    st.markdown('</div>', unsafe_allow_html=True)

    if submit:
        if uploaded_file and doc_identita and identificativo and conferma_firma:
            seed = uploaded_file.getvalue() + doc_identita.getvalue() + identificativo.encode() + luogo_firma.encode()
            final_hash = hashlib.sha256(seed).hexdigest()
            
            nuovo_atto = {
                "nome": nome_atto if nome_atto else uploaded_file.name,
                "identificativo": identificativo,
                "hash": final_hash,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "luogo": luogo_firma,
                "stato": "✅ FIRMATO E VALIDATO"
            }
            
            st.session_state.blockchain.append(nuovo_atto)
            st.success(f"✅ Atto sigillato a {luogo_firma}! Fascicolo digitale protetto.")
            st.balloons()
        else:
            st.warning("⚠️ Compila tutti i campi, carica i documenti e conferma con la firma.")

st.sidebar.info(f"Località predefinita: {luogo_firma if 'luogo_firma' in locals() else 'Milano'}")
