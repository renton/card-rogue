from ..settings import *

class AbstractCard():

    def __init__(self):
        self.flipped = False
        self.locked = False

    def turn_card(self):
        self.flipped = True

    def is_locked(self):
        return self.locked

    def unlock(self):
        self.locked = False

    # debug
    def debug_print(self):
        print "ABSTRACT"
