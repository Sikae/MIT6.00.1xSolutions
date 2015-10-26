__author__ = 'm'


def unique_values(a_dict):

    unique = []

    for key, value in a_dict.items():
        if list(a_dict.values()).count(value) == 1:
            unique.append(key)

    return unique
