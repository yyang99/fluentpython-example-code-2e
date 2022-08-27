import random
from functools import partial

def dice(n):
    return random.randint(1, n)

def d6():
    return partial(dice, 6)()

if __name__ == '__main__':
    d6_iter = iter(d6, 1)
    print(repr(d6_iter))
    for i in d6_iter:
        print(i)