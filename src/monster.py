from settings import *

class Monster():

    def __init__(self):
        self.hp = 10
        self.dmg = 1
        self.alive = True
        
        self.first_strike_roll = 4
        self.overpower_roll = 6

        self.element_resist = {}
        self.element_weak = {}

        self.ko_items = {
                        "bows":1,
                        "wands":1,
                        "swords":1,
                    }

    def is_alive(self):
        return self.alive

    def ko_damage(self):
        self.hp = 0
        self._die()

    def take_damage(self,damage):
        self.hp -= damage

        if self.hp <= 0:
            self._die()

    def _die(self):
        self.hp = 0
        self.alive = False

    # debug
    def __str__(self):
        return "HP: "+str(self.hp)+" FS: "+str(self.first_strike_roll)+" OP: "+str(self.overpower_roll)+" RESIST: "+str(self.element_resist)+" WEAK: "+str(self.element_weak)+" KO: "+str(self.ko_items)
