#! python3

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None

    def setBefore(self, before):
        self.before = before

    def setAfter(self, after):
        self.after = after

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def myName(self):
        return self.name


def insert(at_me, new_frob):
    """
    :param at_me: a Frob that is part of a doubly linked list
    :param new_frob:  a Frob with no links 
    This procedure appropriately inserts new_frob into the linked list that at_me is a part of.
    """

    while True:
        if at_me.name <= new_frob.name:
            frob_after_current = at_me.getAfter()
            if frob_after_current is None:
                at_me.setAfter(new_frob)
                new_frob.setBefore(at_me)
                break

            if frob_after_current.name >= new_frob.name or new_frob.name == at_me.name:
                at_me.setAfter(new_frob)
                new_frob.setBefore(at_me)
                frob_after_current.setBefore(new_frob)
                new_frob.setAfter(frob_after_current)
                break

            at_me = frob_after_current
        else:
            frob_before_current = at_me.getBefore()
            if frob_before_current is None:
                at_me.setBefore(new_frob)
                new_frob.setAfter(at_me)
                break

            if frob_before_current.name <= new_frob.name:
                at_me.setBefore(new_frob)
                new_frob.setAfter(at_me)
                frob_before_current.setAfter(new_frob)
                new_frob.setBefore(frob_before_current)
                break

            at_me = frob_before_current


def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    if start.getBefore() is None:
        return start

    return findFront(start.getBefore)
