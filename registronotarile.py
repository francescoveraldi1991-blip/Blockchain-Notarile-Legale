import streamlit as st
import hashlib
import datetime

# Versione Ultra-Light per evitare crash del browser
st.set_page_config(page_title="Notaio Light", layout="centered")

if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

st.title("⚖️ Notaio Digitale (Versione Stabile)")

menu = ["Notarizza", "Ricerca CF", "Registro"]
scelta = st.sidebar.radio("Menu", menu)

# --- FUNZIONE NOTARIZZA CON FORM (Evita i salti grafici) ---
if scelta == "Notarizza":
    st.header("📄 Nuovo Atto")
    
    with st.form("my_form", clear_on_submit=True):
        nome_atto = st.text_input("Titolo Atto")
        cf_soggetto = st.text_input("Codice Fiscale").upper()
        file_caricato = st.file_uploader("Carica PDF", type=["pdf"])
        consenso = st.checkbox("Confermo identificazione AML/GDPR")
        
        submit = st.form_submit_button("SIGILLA ATTO")
        
        if submit:
            if file_caricato and nome_atto and cf_soggetto and consenso:
                impronta = hashlib.sha256(file_caricato.getvalue()).hexdigest()
                st.session_state.blockchain.append({
                    "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "cf": cf_soggetto,
                    "atto": nome_atto,
                    "hash": impronta
                })
                st.success("✅ Atto registrato!")
            else:
                st.error("❌ Compila tutti i campi e spunta il consenso.")

# --- RICERCA SEMPLIFICATA ---
elif scelta == "Ricerca CF":
    st.header("🔍 Ricerca")
    cerca_cf = st.text_input("Inserisci CF").upper()
    if cerca_cf:
        risultati = [b for b in st.session_state.blockchain if b['cf'] == cerca_cf]
        for r in risultati:
            st.write(f"**{r['data']}** - {r['atto']}")
            st.code(r['hash'])

# --- REGISTRO LEGGERO ---
elif scelta == "Registro":
    st.header("📜 Registro")
    for b in reversed(st.session_state.blockchain):
        st.write(f"ID: {b['cf']} | Atto: {b['atto']} | Data: {b['data']}")
