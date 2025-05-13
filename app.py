import streamlit as st
from deck import Deck
from player import Player

st.set_page_config(page_title="Blackjack", layout="centered")

# 🔄 Inizializzazione session_state
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "deck" not in st.session_state:
    st.session_state.deck = Deck()
if "player" not in st.session_state:
    st.session_state.player = Player("Giocatore")
if "dealer" not in st.session_state:
    st.session_state.dealer = Player("Dealer")
if "bet" not in st.session_state:
    st.session_state.bet = 1
if "in_game" not in st.session_state:
    st.session_state.in_game = False
if "result" not in st.session_state:
    st.session_state.result = ""
if "stats" not in st.session_state:
    st.session_state.stats = {"giocate": 0, "vittorie": 0, "sconfitte": 0, "pareggi": 0}
if "last_card" not in st.session_state:
    st.session_state.last_card = None

# 🎯 Funzione per avviare nuova partita
def reset_game():
    st.session_state.deck = Deck()
    st.session_state.player = Player("Giocatore")
    st.session_state.dealer = Player("Dealer")
    for _ in range(2):
        st.session_state.player.add_card(st.session_state.deck.draw_card())
        st.session_state.dealer.add_card(st.session_state.deck.draw_card())
    st.session_state.in_game = True
    st.session_state.result = ""
    st.session_state.last_card = None

# 📋 Funzione per concludere partita
def end_game():
    dealer = st.session_state.dealer
    while dealer.calculate_points() < 17:
        dealer.add_card(st.session_state.deck.draw_card())

    p_points = st.session_state.player.calculate_points()
    d_points = dealer.calculate_points()
    st.session_state.stats["giocate"] += 1

    if p_points > 21:
        st.session_state.balance -= st.session_state.bet
        st.session_state.result = "Hai sballato! ❌"
        st.session_state.stats["sconfitte"] += 1
    elif d_points > 21 or p_points > d_points:
        st.session_state.balance += st.session_state.bet
        st.session_state.result = "Hai vinto! 🎉"
        st.session_state.stats["vittorie"] += 1
    elif p_points == d_points:
        st.session_state.result = "Pareggio. ⚖️"
        st.session_state.stats["pareggi"] += 1
    else:
        st.session_state.balance -= st.session_state.bet
        st.session_state.result = "Hai perso. 😞"
        st.session_state.stats["sconfitte"] += 1

    st.session_state.in_game = False

# 🧩 Interfaccia utente
st.title("🃏 Blackjack Web Game")
st.write(f"💰 Saldo attuale: **{st.session_state.balance} monete**")

if not st.session_state.in_game:
    st.session_state.bet = st.number_input("Quanto vuoi puntare?", min_value=1, max_value=st.session_state.balance, value=1, step=1)
    if st.button("Inizia partita"):
        reset_game()

if st.session_state.in_game:
    st.subheader("🃤 Le tue carte:")
    st.write(st.session_state.player.show_hand())
    st.write(f"Totale: **{st.session_state.player.calculate_points()} punti**")

    if st.session_state.last_card:
        st.info(f"Hai pescato: **{st.session_state.last_card}**")

    st.subheader("🤖 Carte del dealer:")
    if st.session_state.in_game:
        st.write("[??]", *(str(c) for c in st.session_state.dealer.hand[1:]))
    else:
        st.write(st.session_state.dealer.show_hand())
        st.write(f"Totale: {st.session_state.dealer.calculate_points()} punti")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Pesca carta"):
            new_card = st.session_state.deck.draw_card()
            st.session_state.player.add_card(new_card)
            st.session_state.last_card = new_card
            if st.session_state.player.calculate_points() > 21:
                end_game()
    with col2:
        if st.button("Stai"):
            st.session_state.last_card = None
            end_game()

if st.session_state.result:
    st.markdown("---")
    st.subheader("📢 Risultato finale:")
    st.success(st.session_state.result)
    st.write(f"Carte del dealer: {st.session_state.dealer.show_hand()} — {st.session_state.dealer.calculate_points()} punti")
    st.write(f"Carte del giocatore: {st.session_state.player.show_hand()} — {st.session_state.player.calculate_points()} punti")
    if st.button("Nuova partita"):
        reset_game()

# 📊 Statistiche
with st.expander("📊 Statistiche"):
    st.write(st.session_state.stats)
