__author__ = 'DELL'

spam = ['apples', 'bananas', 'tofu', 'cats']


def separate_items_by_commas(items):
    string = ""
    for i in items:
        if i == items[-1]:
            string += " and " + i + "."
        else:
            string += i + ","
    return string


print(separate_items_by_commas(spam))
