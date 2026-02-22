import streamlit as st
import hashlib
import datetime

st.set_page_config(page_title="Notaio Blockchain", page_icon="⚖️")

st.title("⚖️ Sistema Notarile Blockchain")
st.subheader("Certificazione Contratti e Testamenti Digitali")

# Inizializziamo la "catena" nella memoria della pagina
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

nome_atto = st.text_input("Nome dell'Atto (es. Rep. 101 / Testamento Rossi)")
testo_atto = st.text_area("Contenuto del Contratto o Impronta Hash")

if st.button("Registra Atto con Data Certa"):
    if nome_atto and testo_atto:
        # Calcolo Hash e Data
        data_ora = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        impronta = hashlib.sha256(testo_atto.encode()).hexdigest()
        
        # Salvataggio nel registro
        nuovo_blocco = {
            "indice": len(st.session_state.blockchain) + 1,
            "nome": nome_atto,
            "data": data_ora,
            "hash": impronta
        }
        st.session_state.blockchain.append(nuovo_blocco)
        st.success(f"Atto Registrato con successo! Data certa: {data_ora}")
    else:
        st.error("Per favore, compila tutti i campi.")

st.divider()
st.write("### 📜 Registro degli Atti Notarizzati")
for blocco in reversed(st.session_state.blockchain):
    with st.expander(f"Atto n. {blocco['indice']} - {blocco['nome']}"):
        st.write(f"**Data Certa:** {blocco['data']}")
        st.write(f"**Impronta Digitale (SHA-256):** `{blocco['hash']}`")
