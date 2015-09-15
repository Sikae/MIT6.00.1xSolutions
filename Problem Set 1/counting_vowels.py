__author__ = 'm'

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o',
and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

For problems such as these, do not include input statements or define the variable s in any way. Our automated testing
will provide a value of s for you - so the code you submit in the following box should assume s is already defined.
If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.
"""


def count_vowels(word):
    counter = 0
    for letter in word:
        if letter in "aeiou":
            counter += 1
    return counter

s = input("Enter a string: ")
print("Number of vowels: " + str(count_vowels(s)))
