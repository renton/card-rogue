from settings import *

class Monster():

    def __init__(self):
        self.hp = 1
        self.dmg = 1
        self.alive = True
        
        self.first_strike_roll = 1
        self.overpower_roll = 1

        self.element_resist = {}
        self.element_weak = {}

    def is_alive(self):
        return self.alive

    def take_damage(self,damage):
        self.hp -= damage

        if self.hp <= 0:
            self._die()

    def _die(self):
        self.alive = False

    # debug
    def __str__(self):
        return "HP: "+str(self.hp)+" FS: "+str(self.first_strike_roll)+" OP: "+str(self.overpower_roll)+" RESIST: "+str(self.element_resist)+" WEAK: "+str(self.element_weak)
