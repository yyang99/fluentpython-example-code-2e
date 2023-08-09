"""
explore0.py: Script to explore the OSCON schedule feed

# tag::EXPLORE0_DEMO[]
    >>> import json
    >>> raw_feed = json.load(open('data/osconfeed.json'))
    >>> feed = FrozenJSON(raw_feed)  # <1>
    >>> len(feed.Schedule.speakers)  # <2>
    357
    >>> feed.keys()
    dict_keys(['Schedule'])
    >>> sorted(feed.Schedule.keys())  # <3>
    ['conferences', 'events', 'speakers', 'venues']
    >>> for key, value in sorted(feed.Schedule.items()): # <4>
    ...     print(f'{len(value):3} {key}')
    ...
      1 conferences
    484 events
    357 speakers
     53 venues
    >>> feed.Schedule.speakers[-1].name  # <5>
    'Carina C. Zona'
    >>> talk = feed.Schedule.events[40]
    >>> type(talk)  # <6>
    <class 'explore0.FrozenJSON'>
    >>> talk.name
    'There *Will* Be Bugs'
    >>> talk.speakers  # <7>
    [3471, 5199]
    >>> talk.flavor  # <8>
    Traceback (most recent call last):
      ...
    KeyError: 'flavor'

# end::EXPLORE0_DEMO[]

"""

import json
from collections import abc

class FrozenJSON:
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            FrozenJSON.build(self.__data[name])

    def __dir__(self):
        return self.__data.keys()

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.Sequence):
            return [cls.build(i) for i in obj]
        else:
            return obj

def main():
    raw_feed = json.load(open('data/osconfeed.json'))
    feed = FrozenJSON(raw_feed)
    a = feed.Schedule
    print(a)

if __name__ == '__main__':
    main()
