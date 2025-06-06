import streamlit as st
from partita import Partita

if 'partita' not in st.session_state:
    st.session_state.partita = Partita()

partita = st.session_state.partita
stato = partita.stato()

st.title("🃏 Blackjack - Interfaccia Semplificata")
st.write(f"💰 Saldo: {stato['saldo']} monete")
st.write(f"✅ Vittorie: {stato['vittorie']} | ❌ Sconfitte: {stato['sconfitte']} | 🤝 Pareggi: {stato['pareggi']}")

if stato["storico"]:
    st.subheader("📊 Storico ultime 10 mani")
    for esito, punteggi in stato["storico"]:
        st.write(f"{esito} | Giocatore: {punteggi[0]} - Dealer: {punteggi[1]}")

if stato["saldo"] <= 0:
    st.error("Hai esaurito le monete! Hai perso la partita.")
    st.stop()

if not stato["in_corso"]:
    puntata = st.slider("Scegli la puntata", 1, stato["saldo"], 1)
    if st.button("🎮 Inizia nuova mano"):
        partita.nuova_mano(puntata)
        stato = partita.stato()

if stato["in_corso"]:
    st.subheader("Tua mano:")
    st.write(stato["mano_giocatore"])
    st.write(f"Punteggio: {stato['punteggio_giocatore']}")

    if not stato["fine_mano"]:
        if st.button("🂱 Pesca carta"):
            partita.pesca_giocatore()
            stato = partita.stato()
        if st.button("✋ Stai"):
            partita.stai()
            stato = partita.stato()

    if stato["fine_mano"]:
        st.subheader("Mano del dealer:")
        st.write(stato["mano_dealer"])
        st.write(f"Punteggio dealer: {stato['punteggio_dealer']}")
        st.success(stato["esito"])

        st.button("🔄 Nuova mano")

if st.button("♻️ Reset gioco"):
    del st.session_state["partita"]
    st.experimental_rerun()
