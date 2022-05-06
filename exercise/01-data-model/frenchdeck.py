from typing import NamedTuple
class Card(NamedTuple):
    rank: str
    suits: str

class Deck:
    ranks = [ str(n) for n in range(2, 11)] + list('AJQK')
    suits = "clubs hearts spades diamonds".split()
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

suits_values = {'spades': 4, 'hearts': 3, 'diamonds': 2, 'clubs': 1}

def order_card(card: Card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suits_values) + suits_values[card.suits]

if __name__ == '__main__':
    deck = Deck()
    print(len(deck))
    print(deck[10])
    import random
    print(random.choice(deck))
    print(random.choice(deck))
    print(random.choice(deck))
    print(deck[:3])
    print(Card('Q', 'clubs') in deck)
    sorted_ = sorted(deck, key=order_card)
    print(sorted_)
    print(list(reversed(sorted_)))

