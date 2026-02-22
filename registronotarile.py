import streamlit as st

st.set_page_config(page_title="Studio Notarile Digitale", layout="centered")

st.title("⚖️ Benvenuti nello Studio Notarile Blockchain")
st.write("Questo sistema modulare garantisce la massima stabilità e conformità legale.")
st.info("Usa il menu a sinistra per navigare tra le diverse sezioni del software.")

# Inizializziamo il registro una sola volta per tutte le pagine
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []
