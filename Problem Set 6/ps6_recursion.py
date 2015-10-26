# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#


def reverse_string(string):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    string: a string
    returns: a reversed string
    """
    if len(string) == 1:
        return string

    return string[-1] + reverse_string(string[:-1])


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

    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    


#
# Problem 5: Typewriter
#
def insert_new_lines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    pass


def main():
    print(reverse_string("Hello"))

if __name__ == '__main__':
    main()