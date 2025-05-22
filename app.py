
import streamlit as st
from partita import Partita

# Inizializzazione della sessione
if 'partita' not in st.session_state:
    st.session_state.partita = Partita()
if 'puntata' not in st.session_state:
    st.session_state.puntata = 1
if 'esito' not in st.session_state:
    st.session_state.esito = ""
if 'mano_mostrata' not in st.session_state:
    st.session_state.mano_mostrata = False

st.title("🃏 Blackjack con sistema a puntate")

giocatore = st.session_state.partita.giocatore

st.write(f"💰 Saldo attuale: {giocatore.saldo} monete")
st.write(f"📉 Partite perse: {giocatore.sconfitte}")

st.slider("Scegli la puntata", min_value=1, max_value=giocatore.saldo, key='puntata')

if st.button("Gioca una mano"):
    esito = st.session_state.partita.avvia_mano(st.session_state.puntata)
    st.session_state.esito = esito
    st.session_state.mano_mostrata = True

if st.session_state.mano_mostrata:
    st.subheader("🂠 Mano del Giocatore")
    mano_giocatore = st.session_state.partita.giocatore.mano
    st.write([f"{carta.valore} di {carta.seme}" for carta in mano_giocatore])
    st.write(f"Totale: {st.session_state.partita.giocatore.calcola_punteggio()}")

    st.subheader("🂠 Mano del Dealer")
    mano_dealer = st.session_state.partita.dealer.mano
    st.write([f"{carta.valore} di {carta.seme}" for carta in mano_dealer])
    st.write(f"Totale: {st.session_state.partita.dealer.calcola_punteggio()}")

    st.subheader("📢 Esito")
    st.success(st.session_state.esito)

if st.button("Reset"):
    del st.session_state['partita']
    del st.session_state['puntata']
    del st.session_state['esito']
    del st.session_state['mano_mostrata']
    st.experimental_rerun()
