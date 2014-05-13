from settings import *

class Monster():

    def __init__(
                    self,
                    hp,
                    first_strike_roll,
                    overpower_roll,
                    ko_items,
                    reward,
                ):
        self.hp = hp
        self.dmg = 1
        self.alive = True
        
        self.first_strike_roll = first_strike_roll
        self.overpower_roll = overpower_roll

        self.element_resist = {}
        self.element_weak = {}

        self.ko_items = ko_items
        self.reward = reward

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
        return "HP: "+str(self.hp)+" FS: "+str(self.first_strike_roll)+" OP: "+str(self.overpower_roll)+" RESIST: "+str(self.element_resist)+" WEAK: "+str(self.element_weak)+" KO: "+str(self.ko_items)+" REWARD: "+str(self.reward)
