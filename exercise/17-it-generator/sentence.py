import re
import reprlib
import collections.abc

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.word = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.word[item]

    def __len__(self):
        return len(self.word)

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"

def is_iterable(test_obj):
    try:
        iter(test_obj)
        return True
    except TypeError:
        return False

def is_collection_iterator(test_obj):
    if isinstance(test_obj, collections.abc.Iterator):
        return True
    else:
        return False

if __name__ == '__main__':
    s = Sentence("this is a very long text, some words will be truncated, if the line is too long")
    for word in s:
        print(word)

    print(f"is {s} iterable: {is_iterable(s)}")
    print(f"is {s} a instance of collection Iterator: {is_collection_iterator(s)}")

