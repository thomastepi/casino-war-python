
# Player Class
class Player:
    # initiator
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return f"{self.name} has\nValue: {self.get_hand_value()}\tCard: {self.hand}"

    # get the value of drawn card
    def get_hand_value(self):
        value = self.hand[0].value
        return value

    # discard drawn cards
    def empty_hand(self):
        self.hand = []

    # draw card from deck
    def get_card(self, card):
        self.hand.append(card)
