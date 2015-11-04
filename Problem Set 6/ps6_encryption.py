# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORD_LIST_FILENAME = "words.txt"


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    in_file = open(WORD_LIST_FILENAME)
    word_list = in_file.read().split()
    print("  ", len(word_list), "words loaded.")
    return word_list


def is_word(word_list, word):
    """
    Determines if word is a valid word.

    :param word_list: list of words in the dictionary.
    :param word: a possible word.
    :returns: True if word is in word_list.
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in word_list


def random_word(word_list):
    """
    Returns a random word.

    :param word_list: list of words
    :returns: a word from word_list at random
    """
    return random.choice(word_list)


def random_string(word_list, n):
    """
    Returns a string containing n random words from word_list

    :param word_list: list of words
    :returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(word_list) for _ in range(n)])


def random_scrambled(word_list, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    :param word_list: list of words
    :param n: number of random words to generate and scamble
    :returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = random_string(word_list, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i - 1] == ' ']
    return apply_shift(s, shifts)[:-1]


def get_story_string():
    """
    :returns: a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#


def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    :param shift: 0 <= int < 26
    :returns: dict
    """
    pass


def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    :param text: string
    :param coder: dict with mappings of characters to shifted characters
    :returns: text after mapping coder chars to original text
    """
    pass


def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    :param text: string to apply the shift to
    :param shift: amount to shift the text (0 <= int < 26)
    :returns: text after being shifted by specified amount.
    """
    pass


#
# Problem 2: Decryption
#
def find_best_shift(word_list, text):
    """
    Finds a shift key that can decrypt the encoded text.

    :param word_list: a lists of words
    :param text: string
    :returns: 0 <= int < 26
    """
    pass


def decrypt_story():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function get_story_string().
    Use the functions get_story_string and loadWords to get the
    raw data you need.

    :returns: string - story in plain text
    """
    pass


#
# Build data structures used for entire session and run encryption
#

def main():
    print(decrypt_story())


if __name__ == '__main__':
    main()
