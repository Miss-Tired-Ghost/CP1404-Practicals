"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def set_sentence_format(sentence: str):
    """
    Capitalise first letter, end with a full stop.
    >>> set_sentence_format('hello')
    'Hello.'

    Do not change correct formatting.
    >>> set_sentence_format('It is an ex parrot.')
    'It is an ex parrot.'

    Capitalise first letter.
    >>> set_sentence_format('coding is sometimes spaghetti.')
    'Coding is sometimes spaghetti.'

    End with a full stop.
    >>> set_sentence_format('Tests are great')
    'Tests are great.'

    Allow alternate end characters.
    >>> set_sentence_format('Exclamation marks are loud!')
    'Exclamation marks are loud!'
    """
    if sentence[-1:] not in [".", "!", "?"]:
        sentence += "."
    return sentence.capitalize()


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"
    assert car.fuel == 0

    car = Car(fuel=10)
    assert car.fuel == 10


run_tests()
doctest.testmod()
