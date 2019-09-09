import json
from typing import Iterator, Text
from itertools import zip_longest
from pathlib import Path


def grouper(n, iterable, padvalue=None) -> Iterator:
    return zip_longest(*[iter(iterable)] * n, fillvalue=padvalue)


def translate_char(char) -> Text:
    names = {
        'd': 'diamond',
        'h': 'heart',
        'c': 'club',
        's': 'spade',
        'o': 'open',
        'n': None
    }
    return names[char]


def main():
    with open(Path('dataset.txt')) as dataset_file:
        data_string = dataset_file.readline()

    card_strings = grouper(8, data_string, 'x') # x will cause a keyerror in translate_char if present
    cards = []
    for card_string in card_strings:
        card = []
        for char in card_string:
            card.append(translate_char(char))
        cards.append(card)

    with open(Path('cards.json'), 'w') as out_file:
        json.dump(cards, out_file, indent=4)


if __name__ == '__main__':
    main()
