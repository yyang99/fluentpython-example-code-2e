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

if __name__ == '__main__':
    deck = Deck()
    print(len(deck))
    print(deck[10])