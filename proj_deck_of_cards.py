from modules.printutils import *
from random import randint, shuffle

# for later…
# ♣ ♥ ♠ ♦

class Card:

    valid_values = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
    valid_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    suit_symbols = {
        "Clubs": "♣", 
        "Hearts": "♥", 
        "Spades": "♠", 
        "Diamonds": "♦"
    }

    # Original
    # def __repr__(self):
        # return f"{self.value} of {self.suit}"
    def __repr__(self):
        return f"{Card.suit_symbols.get(self.suit)}{self.value}"

    def __init__(self, suit, value):
        # suit is valid ?
        if suit not in Card.valid_suits:
            raise ValueError(f"\n{suit} is not a valid suit. Choose from {', '.join(Card.valid_suits)}.")
        # card value is valid ?
        if value not in Card.valid_values:
            raise ValueError(f"\n{value} is not a valid card value. Choose from {', '.join(Card.valid_values)}.")
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
        # return [self.cards.pop(randint(0, self.count()-1)) 
        #     for card in range(0,min(self.count(), num_cards))
        return [self.cards.pop() for card in range(0, num_cards)]

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
# should throw a ValueError
# h11 = Card("Hearts", "11")

pl(
    h5, hQ, s2, c9, h6
)

banner("""Testing Deck""")

deck = Deck()

banner("""Printing the deck""")
# ------------------------------
pl(deck)

banner("""Printing the cards in the deck""")
# ------------------------------
pl(deck.cards)

banner("""Shuffling and printing the cards in the deck""")
# ------------------------------
deck.shuffle()
pl(deck.cards)

banner("""Here's the current deck after shuffling""")
# ------------------------------
pl(deck)

banner("""Dealing one card""")
# ------------------------------
pl(deck.deal_card())

banner("""Dealing a hand""")
# ------------------------------
pl(deck.deal_hand(7))

banner("""The current deck again""")
# ------------------------------
pl(deck)
