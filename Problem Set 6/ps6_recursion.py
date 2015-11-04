# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
import string


def reverse_string(character_string):
    """
    Given a character_string, recursively returns a reversed copy of the character_string.
    For example, if the character_string is 'abc', the function returns 'cba'.
    The only character_string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    :param character_string: a character_string
    :returns: a reversed character_string
    """
    pass


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    x_ian('eric', 'meritocracy') -> True
    x_ian('eric', 'cerium') -> False
    x_ian('john', 'mahjong') -> False

    :param x: a string
    :param word: a string
    :returns: True if word is x_ian, False otherwise
    """
    pass


#
# Problem 5: Typewriter
#
def insert_new_lines(text, line_length):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    :param text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    :returns: a string, with newline characters inserted appropriately.
    """
    pass


def main():
    print(reverse_string("Hello"))
    print(x_ian('eric', 'meritocracy'))
    print(x_ian('eric', 'cerium'))
    print(x_ian('john', 'mahjong'))
    print(x_ian("roberto", "crooooootttttbpppefadfdarsssst111oppp"))
    print(insert_new_lines("Russian submarines and spy ships are aggressively operating near the vital undersea "
                           "cables that carry almost all global Internet communications, raising concerns among some "
                           "American military and intelligence officials that the Russians might be planning to attack "
                           "those lines in times of tension or conflict. The issue goes beyond old worries during the "
                           "Cold War that the Russians would tap into the cables  a task American intelligence "
                           "agencies also mastered decades ago. The alarm today is deeper: The ultimate Russian hack "
                           "on the United States could involve severing the fiber-optic cables at some of their "
                           "hardest-to-access locations to halt the instant communications on which the West's "
                           "governments, economies and citizens have grown dependent.", 40))


if __name__ == '__main__':
    main()
