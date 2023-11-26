"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join(s for i in range(n))


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


def make_sentence(phrase):
    """
    Make a phrase into a sentence by change the first letter to capital and addin a fullstop at the end.
    >>> make_sentence("hello")
    'Hello.'
    >>> make_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> make_sentence("to be or not to be")
    'To be or not to be.'
    """
    sentence = phrase[0].upper() + phrase[1:]
    if sentence[-1] != ".":
        sentence += "."
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car("Prius")
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car("Prius")
    assert test_car.fuel == 0, "Car does not set fuel correctly"  # test for default value
    test_car = Car("Prius", fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"  # test for value passed in


run_tests()

doctest.testmod()
