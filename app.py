import streamlit as st
from partita import Partita

# Inizializza la partita se non esiste già
if 'partita' not in st.session_state:
    st.session_state.partita = Partita()

partita = st.session_state.partita
stato = partita.stato()

# Titolo
st.title("🃏 Blackjack - Interfaccia Semplificata")

# Saldo e statistiche (usiamo .get per evitare KeyError)
st.write(f"💰 Saldo: {stato.get('saldo', 0)} monete")
st.write(f"✅ Vittorie: {stato.get('vittorie', 0)} | ❌ Sconfitte: {stato.get('sconfitte', 0)} | 🤝 Pareggi: {stato.get('pareggi', 0)}")

# Storico partite
if stato.get("storico"):
    st.subheader("📊 Storico ultime 10 mani")
    for esito, punteggi in stato["storico"]:
        st.write(f"{esito} | Giocatore: {punteggi[0]} - Dealer: {punteggi[1]}")

# Fine gioco se il saldo è 0
if stato.get("saldo", 0) <= 0:
    st.error("Hai esaurito le monete! Hai perso la partita.")
    st.stop()

# Nuova mano
if not stato.get("in_corso", False):
    puntata = st.slider("Scegli la puntata", 1, stato.get("saldo", 1), 1)
    if st.button("🎮 Inizia nuova mano"):
        partita.nuova_mano(puntata)
        st.rerun()

# Mano in corso
if stato.get("in_corso", False):
    st.subheader("Tua mano:")
    st.write([str(c) for c in stato.get("mano_giocatore", [])])
    st.write(f"Punteggio: {stato.get('punteggio_giocatore', 0)}")

    if not stato.get("fine_mano", False):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🂱 Pesca carta"):
                partita.pesca_giocatore()
                st.rerun()
        with col2:
            if st.button("✋ Stai"):
                partita.stai()
                st.rerun()

    if stato.get("fine_mano", False):
        st.subheader("Mano del dealer:")
        st.write([str(c) for c in stato.get("mano_dealer", [])])
        st.write(f"Punteggio dealer: {stato.get('punteggio_dealer', 0)}")
        st.success(stato.get("esito", ""))
        st.button("🔄 Nuova mano")

# Pulsante per reset
if st.button("♻️ Reset gioco"):
    del st.session_state["partita"]
    st.rerun()
