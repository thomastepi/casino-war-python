from random import shuffle

# You can change which suite is higher, by changing the order in this list.
# The last one is highest, the first is lowest.
SUITES = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
VALUES = {14: 'Ace', 13: 'King', 12: 'Queen', 11: 'Jack'}
ACE_HIGH = True  # Decides is Ace is the highest or lowest card


class Deck:
    def __init__(self):
        self.cards = []
        self.reset_deck()

    def reset_deck(self):
        self.cards = []
        for s in SUITES:
            for v in range(2, 14):
                self.cards.append(Card(v, s))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def __repr__(self):
        return f"This deck has {len(self.cards)} cards."

    def contains_card(self, card):
        for c in self.cards:
            if c == card:
                return True
        return False


class Card:
    def __init__(self, value, suite):
        self.suite = suite
        self.value = value

    def __repr__(self):
        return f'{self.value if self.value not in VALUES.keys() else VALUES[self.value]} of {self.suite}'

    def match_suite(self, other):
        return self.suite == other.suite

    def match_value(self, other):
        return self.value == other.value

    def has_higher_value_than(self, other):
        if ACE_HIGH:
            mine = self.value if self.value != 1 else 14
            not_mine = other.value if other.value != 1 else 14
        return mine > not_mine

    def has_higher_suite_than(self, other):
        return SUITES.index(self.suite) > SUITES.index(other.suite)

    def __eq__(self, other) -> bool:
        return self.value == other.value and self.suite == other.suite
