from deck import Deck
from player import Player


# ask player if he wishes to end game or keep playing
def ask(question):
    if (input(question).lower()) == 'e':
        return True
    else:
        return False


# display the values of drawn cards of player and dealer
def print_game_state(player, dealer):
    print("=======Result========")
    print(player)
    print(dealer)
    print("====================")


# player suspends in the case of a tie
def tie_situation():
    print("It's a tie! You suspend, so u lose half your bet")
    return False


# compare values of drawn cards of player and dealer and determines if player wins
def get_winner(player, dealer):
    if player.get_hand_value() > dealer.get_hand_value():
        return True
    if player.get_hand_value() < dealer.get_hand_value():
        return False
    else:
        tie_situation()


# main method
def main():
    deck = Deck()
    cards = deck.cards
    deck.shuffle()
    player = Player(input("enter your name: "))
    dealer = Player("Dealer")
    while len(cards) >= 2:
        if ask("Press Enter to keep playing or press E to exit..."):
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
