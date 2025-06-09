import streamlit as st
from partita import Partita

# Inizializza la partita se non esiste già
if 'partita' not in st.session_state:
    st.session_state.partita = Partita()

partita = st.session_state.partita
stato = partita.stato()

# Titolo
st.title("🃏 Blackjack")

# Saldo e statistiche
st.write(f"💰 Saldo: {stato['saldo']} monete")
st.write(f"✅ Vittorie: {stato['vittorie']} | ❌ Sconfitte: {stato['sconfitte']} | 🤝 Pareggi: {stato['pareggi']}")

# Storico partite
if stato["storico"]:
    st.subheader("📊 Storico ultime 10 mani")
    for esito, punteggi in stato["storico"]:
        st.write(f"{esito} | Giocatore: {punteggi[0]} - Dealer: {punteggi[1]}")

# Fine gioco se il saldo è 0
if stato["saldo"] <= 0:
    st.error("Hai esaurito le monete! Hai perso la partita.")
    st.stop()

# Nuova mano
if not stato["in_corso"]:
    puntata = st.slider("Scegli la puntata", 1, stato["saldo"], 1)
    if st.button("🎮 Inizia nuova mano"):
        partita.nuova_mano(puntata)
        st.rerun()

# Mano in corso
if stato["in_corso"]:
    st.subheader("Tua mano:")
    st.write([str(c) for c in stato["mano_giocatore"]])
    st.write(f"Punteggio: {stato['punteggio_giocatore']}")

    if not stato["fine_mano"]:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🂱 Pesca carta"):
                partita.pesca_giocatore()
                st.rerun()
        with col2:
            if st.button("✋ Stai"):
                partita.stai()
                st.rerun()

    if stato["fine_mano"]:
        st.subheader("Mano del dealer:")
        st.write([str(c) for c in stato["mano_dealer"]])
        st.write(f"Punteggio dealer: {stato['punteggio_dealer']}")
        st.success(stato["esito"])
        st.button("🔄 Nuova mano")

# Pulsante per reset
if st.button("♻️ Reset gioco"):
    del st.session_state["partita"]
    st.rerun()

