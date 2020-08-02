from random import randint, shuffle

# ------------------------------
#   Card
# ------------------------------
class Card:

    valid_values = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
    valid_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    suit_symbols = {
        "Clubs": "♣", 
        "Hearts": "♥", 
        "Spades": "♠", 
        "Diamonds": "♦"
    }

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


# ------------------------------
#   Deck
#
#   dependendies:
#       Card
# ------------------------------
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
