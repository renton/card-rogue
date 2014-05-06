from ..settings import *

class AbstractCard():

    def __init__(self):
        self.flipped = False
        self.locked = False
        self.actions = {}
        self.name = "ABSTRACT"

    def turn_card(self,hero):
        self.flipped = True

    def is_locked(self):
        return self.locked

    def unlock(self):
        self.locked = False

    def action(self,hero):
        pass

    def disable_action(self,action):
        self.actions[action]["enabled"] = False

    def is_action_enabled(self,action):
        return self.actions[action]["enabled"]

    # debug
    def debug_print(self):
        print "ABSTRACT"
