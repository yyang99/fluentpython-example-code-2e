# 1. class variables, vs object variables
    class Deck:
        ranks = [ str(n) for n in range(2, 11)] + list('AJQK')
        suits = "clubs hearts spades diamonds".split()
        def __init__(self):
            self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

# 2. list(\<iterable>)
    >>> a = 'abcd'
    >>> list(a)
    ['a', 'b', 'c', 'd']
    
    
    >>> for i in a:
    ...     print(i)
    ...     
    a
    b
    c
    d
    
    
    >>> ai = a.__iter__()
    >>> next(ai)
    'a'
    >>> next(ai)
    'b'
    >>> next(ai)
    'c'
    >>> next(ai)
    'd'
    >>> next(ai)
    Traceback (most recent call last):
      File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/code.py", line 90, in runcode
        exec(code, self.locals)
      File "<input>", line 1, in <module>
    StopIteration

# 3. \__len__ and \__getitem__ enable python collection functions such as iteration, contain
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

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

##  \__len__()
### use len(collection) instead of collection.len().
## \__getitem__() 
### obj[key] is supported by the \__getitem__ special method
### by implementing the \__getitem__ special method, our deck is also iterable, Iteration is often implicit. If a collection has no __contains__ method, the in opera‐tor does a sequential scan
### our \__getitem__ delegates to the [] operator of self._cards, our deck automatically supports slicing

## 4. define a key function for 
    suits_values = {'spades': 4, 'hearts': 3, 'diamonds': 2, 'clubs': 1}
    
    def order_card(card: Card):
        rank_value = Deck.ranks.index(card.rank)
        return rank_value * len(suits_values) + suits_values[card.suits]

### Note: list.index(x)

## 5. difference between list.sort() and sorted()
https://www.30secondsofcode.org/articles/s/python-sortedlist-vs-list-sort

The primary difference between the two is that list.sort() will sort the list in-place, mutating its indexes and returning None, whereas sorted() will return a new sorted list leaving the original list unchanged. Another difference is that sorted() accepts any iterable while list.sort() is a method of the list class and can only be used with lists

    nums = [2, 3, 1, 5, 6, 4, 0]
    
    print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
    print(nums)           # [2, 3, 1, 5, 6, 4, 0]
    
    print(nums.sort())    # None
    print(nums)           # [0, 1, 2, 3, 4, 5, 6]

### When to use each one
list.sort() should be used whenever mutating the list is intended and retrieving the original order of the elements is not desired. On the other hand, sorted() should be used when the object to be sorted is an iterable (e.g. list, tuple, dictionary, string) and the desired outcome is a sorted list containing all elements.

