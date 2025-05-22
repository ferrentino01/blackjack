
import streamlit as st
import random

# ===================== CLASSI =====================

class Carta:
    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def get_valore_numerico(self):
        if self.valore in ['J', 'Q', 'K']:
            return 10
        elif self.valore == 'A':
            return 11
        else:
            return int(self.valore)

    def __str__(self):
        return f"{self.valore} di {self.seme}"

class Mazzo:
    semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
    valori = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.carte = [Carta(seme, valore) for seme in self.semi for valore in self.valori]
        random.shuffle(self.carte)

    def pesca(self):
        return self.carte.pop() if self.carte else None

class Tavolo:
    def __init__(self):
        self.carte_giocatore = []
        self.carte_dealer = []

    def reset(self):
        self.carte_giocatore = []
        self.carte_dealer = []

    def aggiungi_giocatore(self, carta):
        self.carte_giocatore.append(carta)

    def aggiungi_dealer(self, carta):
        self.carte_dealer.append(carta)

    def mostra_mano(self, tipo):
        if tipo == "giocatore":
            return [str(c) for c in self.carte_giocatore]
        elif tipo == "dealer":
            return [str(c) for c in self.carte_dealer]

def calcola_punteggio(mano):
    totale = 0
    assi = 0
    for carta in mano:
        valore = carta.get_valore_numerico()
        totale += valore
        if carta.valore == 'A':
            assi += 1
    while totale > 21 and assi:
        totale -= 10
        assi -= 1
    return totale

# ===================== INIZIALIZZAZIONE STATO =====================

if 'saldo' not in st.session_state:
    st.session_state.saldo = 1000
    st.session_state.vittorie = 0
    st.session_state.sconfitte = 0
    st.session_state.pareggi = 0
    st.session_state.storico = []
    st.session_state.mazzo = Mazzo()
    st.session_state.tavolo = Tavolo()
    st.session_state.in_corso = False
    st.session_state.puntata = 1
    st.session_state.fine_mano = False
    st.session_state.hit = False

# ===================== INTERFACCIA =====================

st.title("🃏 Blackjack - Tavolo Edition")
st.write(f"💰 Saldo: {st.session_state.saldo} monete")
st.write(f"✅ Vittorie: {st.session_state.vittorie} | ❌ Sconfitte: {st.session_state.sconfitte} | 🤝 Pareggi: {st.session_state.pareggi}")

# Storico ultime 10
if st.session_state.storico:
    st.subheader("📊 Storico ultime 10 mani")
    for esito, punteggi in st.session_state.storico[-10:][::-1]:
        st.write(f"{esito} | Giocatore: {punteggi[0]} - Dealer: {punteggi[1]}")

# ===================== GIOCO =====================

if not st.session_state.in_corso:
    st.session_state.puntata = st.slider("Scegli la puntata", 1, st.session_state.saldo, 1)
    if st.button("🎮 Inizia nuova mano"):
        st.session_state.tavolo.reset()
        for _ in range(2):
            carta_g = st.session_state.mazzo.pesca()
            carta_d = st.session_state.mazzo.pesca()
            st.session_state.tavolo.aggiungi_giocatore(carta_g)
            st.session_state.tavolo.aggiungi_dealer(carta_d)
        st.session_state.in_corso = True
        st.session_state.fine_mano = False
        st.session_state.hit = False
        st.session_state.saldo -= st.session_state.puntata

if st.session_state.in_corso:
    st.subheader("Tua mano:")
    mano_giocatore = st.session_state.tavolo.carte_giocatore
    st.write(st.session_state.tavolo.mostra_mano("giocatore"))
    punteggio_giocatore = calcola_punteggio(mano_giocatore)
    st.write(f"Punteggio: {punteggio_giocatore}")

    if not st.session_state.fine_mano:
        if st.button("🂱 Pesca carta"):
            st.session_state.hit = True
        if st.button("✋ Stai"):
            st.session_state.fine_mano = True

    if st.session_state.hit and not st.session_state.fine_mano:
        nuova = st.session_state.mazzo.pesca()
        st.session_state.tavolo.aggiungi_giocatore(nuova)
        st.session_state.hit = False

        punteggio_giocatore = calcola_punteggio(mano_giocatore)
        if punteggio_giocatore > 21:
            st.session_state.sconfitte += 1
            st.session_state.storico.append(("❌ Sconfitta (sballato)", (punteggio_giocatore, calcola_punteggio(st.session_state.tavolo.carte_dealer))))
            st.error("Hai sballato! Hai perso.")
            st.session_state.fine_mano = True
            st.session_state.in_corso = False

    if st.session_state.fine_mano:
        while calcola_punteggio(st.session_state.tavolo.carte_dealer) < 17:
            st.session_state.tavolo.aggiungi_dealer(st.session_state.mazzo.pesca())

        punteggio_dealer = calcola_punteggio(st.session_state.tavolo.carte_dealer)

        st.subheader("Mano del dealer:")
        st.write(st.session_state.tavolo.mostra_mano("dealer"))
        st.write(f"Punteggio dealer: {punteggio_dealer}")

        if punteggio_giocatore > 21:
            pass
        elif punteggio_dealer > 21 or punteggio_giocatore > punteggio_dealer:
            st.success("Hai vinto!")
            st.session_state.vittorie += 1
            st.session_state.saldo += st.session_state.puntata * 2
            st.session_state.storico.append(("✅ Vittoria", (punteggio_giocatore, punteggio_dealer)))
        elif punteggio_giocatore == punteggio_dealer:
            st.info("Pareggio!")
            st.session_state.pareggi += 1
            st.session_state.saldo += st.session_state.puntata
            st.session_state.storico.append(("🤝 Pareggio", (punteggio_giocatore, punteggio_dealer)))
        else:
            st.error("Hai perso!")
            st.session_state.sconfitte += 1
            st.session_state.storico.append(("❌ Sconfitta", (punteggio_giocatore, punteggio_dealer)))

        st.session_state.in_corso = False
        st.session_state.hit = False
        st.button("🔄 Nuova mano")

# ===================== RESET =====================
if st.button("♻️ Reset gioco"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()
