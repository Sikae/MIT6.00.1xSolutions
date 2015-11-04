#! python3


class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None

    def set_before(self, before):
        self.before = before

    def set_after(self, after):
        self.after = after

    def get_before(self):
        return self.before

    def get_after(self):
        return self.after

    def my_name(self):
        return self.name


def insert(at_me, new_frob):
    """
    :param at_me: a Frob that is part of a doubly linked list
    :param new_frob:  a Frob with no links 
    This procedure appropriately inserts new_frob into the linked list that at_me is a part of.
    """
    pass


def find_front(start):
    """
    :param start: a Frob that is part of a doubly linked list
    :returns: the Frob at the beginning of the linked list
    """
    pass
