from modules.printutils import *
from random import randint, shuffle

class Card:

    valid_values = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
    valid_suits = ("Hearts", "Diamonds", "Clubs", "Spades")

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __init__(self, suit, value):
        # suit is valid ?
        if suit not in Card.valid_suits:
            raise ValueError(f"{suit} is not a valid suit. Choose from {', '.join(Card.valid_suits)}.")
        # card value is valid ?
        if value not in Card.valid_values:
            raise ValueError(f"{value} is not a valid card value. Choose from {', '.join(Card.valid_values)}.")
        self.suit = suit
        self.value = str(value)

class Deck:

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def __init__(self):
        self.cards = [
            Card(suit, value) for suit in Card.valid_suits 
                for value in Card.valid_values
        ]

    def count(self):
        return len(self.cards)

    def _deal(self, num_cards):
        if self.count() == 0:
            raise ValueError("All cards have been dealt.")
        elif self.count() < num_cards:
            num_cards = self.count()
        return [self.cards.pop(randint(0, self.count()-1)) for card in range(0,num_cards)]

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)
    
    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num_cards):
        return self._deal(num_cards)


banner("""Testing Cards""")

h5 = Card("Hearts", "5")
hQ = Card("Hearts", "Q")
s2 = Card("Spades", "2")
c9 = Card("Clubs", "9")
h6 = Card("Hearts", "6")
pl(
    h5, hQ, s2, c9, h6
)

banner("""Testing Deck""")

deck = Deck()
pl(deck)
pl(deck.cards)
deck.shuffle()
pl(deck.cards)
pl(deck._deal(10))
pl(deck)
pl(deck.deal_card())
pl(deck.deal_hand(7))
# deck.shuffle()
# pl(deck.cards)
# pl(deck._deal(5))
# pl(deck._deal(3))
