class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score1 = 0
        self.score2 = 0

    def __repr__(self):
        return f"{self.name} has\nValue: {self.get_hand_value()}\tCard: {self.hand}"

    def get_hand_value(self):
        value = self.hand[0].value
        return value

    def empty_hand(self):
        self.hand = []

    def get_card(self, card):
        self.hand.append(card)
