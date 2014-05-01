from settings import *

class Monster():

    def __init__(self):
        self.hp = 1
        self.dmg = 1
        
        self.first_strike_roll = 1
        self.overpower_roll = 1

        self.element_resist = {}
        self.element_weak = {}

    # debug
    def __str__(self):
        return "HP: "+str(self.hp)+" FS: "+str(self.first_strike_roll)+" OP: "+str(self.overpower_roll)+" RESIST: "+str(self.element_resist)+" WEAK: "+str(self.element_weak)
