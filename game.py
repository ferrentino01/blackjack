from deck import Deck
from player import Player

def main():
    deck = Deck()
    dealer = Player("Dealer")
    player = Player("Player")

    # Distribuzione iniziale
    for _ in range(2):
        player.add_card(deck.draw_card())
        dealer.add_card(deck.draw_card())

    # Mostra mani
    print(f"Dealer: {dealer.show_hand(hide_first=True)}")
    print(f"{player.name}: {player.show_hand()} ({player.calculate_points()} punti)")

    # Turno del giocatore
    while player.calculate_points() < 21:
        action = input("Vuoi pescare una carta? (s/n): ")
        if action.lower() == 's':
            player.add_card(deck.draw_card())
            print(f"{player.name}: {player.show_hand()} ({player.calculate_points()} punti)")
        else:
            break

    # Turno del dealer
    while dealer.calculate_points() < 17:
        dealer.add_card(deck.draw_card())

    print(f"Dealer: {dealer.show_hand()} ({dealer.calculate_points()} punti)")

    # Esito
    player_pts = player.calculate_points()
    dealer_pts = dealer.calculate_points()
    if player_pts > 21:
        print("Hai sballato. Hai perso!")
    elif dealer_pts > 21 or player_pts > dealer_pts:
        print("Hai vinto!")
    elif player_pts == dealer_pts:
        print("Pareggio.")
    else:
        print("Hai perso.")

if __name__ == "__main__":
    main()
