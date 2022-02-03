from random_word import RandomWords
import string
import random


def randword():
    """
    A simple function which returns a random uppercase word with no punctuation.
    Intended to be concatenated at the end of file names to rapidly make unique filenames with no numbers.
    :return: word
    """

    r = RandomWords()
    try:
        word = str((str(r.get_random_word()).upper()).replace("-", ""))
        while word == "NONE":
            word = str((str(r.get_random_word()).upper()).translate(str.maketrans('', '', string.punctuation)))
    except (RuntimeError, TypeError, NameError, KeyError, ValueError, ModuleNotFoundError):
        # Whoops, here's a random number instead!
        return str(random.randint(100000, 999999))
    return word
