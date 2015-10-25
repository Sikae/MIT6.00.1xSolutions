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

    word_list: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in word_list


def random_word(word_list):
    """
    Returns a random word.

    word_list: list of words
    returns: a word from wordList at random
    """
    return random.choice(word_list)


def random_string(word_list, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(word_list) for _ in range(n)])


def random_scrambled(word_list, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    word_list: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = random_string(word_list, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i - 1] == ' ']
    return apply_shifts(s, shifts)[:-1]


def get_story_string():
    """
    Returns a story in encrypted text.
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

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    return "Not yet implemented."  # Remove this comment when you code the function


def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    return "Not yet implemented."  # Remove this comment when you code the function


def apply_shifts(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return "Not yet implemented."  # Remove this comment when you code the function


#
# Problem 2: Decryption
#
def find_best_shift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    return "Not yet implemented."  # Remove this comment when you code the function


def decrypt_story():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function get_story_string().
    Use the functions get_story_string and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    return "Not yet implemented."  # Remove this comment when you code the function


#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test find_best_shift:
    wordList = load_words()
    s = apply_shifts('Hello, world!', 8)
    bestShift = find_best_shift(wordList, s)
    assert apply_shifts(s, bestShift) == 'Hello, world!'
    # To test decrypt_story, comment the above four lines and uncomment this line:
    #    decrypt_story()
