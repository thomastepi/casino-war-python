from deck import Deck
from player import Player


def ask(question):
    return 'y' in input(question).lower()


def print_game_state(player, dealer):
    print("=======Result========")
    print(player)
    print(dealer)
    print("====================")


def get_winner(player, dealer):
    if player.get_hand_value() > dealer.get_hand_value():
        return True
    if player.get_hand_value() < dealer.get_hand_value():
        return False
    else:
        return "No one"


def main():
    deck = Deck()
    cards = deck.cards
    deck.shuffle()
    player = Player(input("enter your name: "))
    dealer = Player("Dealer")
    while len(cards) >= 2:
        if ask("Do you want to quit? "):
            #print(f"Your final score is {player.score}")
            exit()
        else:
            player.get_card(deck.draw())
            dealer.get_card(deck.draw())

            if get_winner(player, dealer):
                print("YOU HAVE WON!!!")
                print_game_state(player, dealer)
            else:
                print("you lose")
                print_game_state(player, dealer)
            player.empty_hand()
            dealer.empty_hand()
            deck.reset_deck()
            deck.shuffle()


if __name__ == '__main__':
    main()
