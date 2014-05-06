from abstractcard import AbstractCard
from ..settings import *

class TrapCard(AbstractCard):
    # TODO trap can't kill you. can only take you down to 1 hp

    def __init__(self,damage): 
        AbstractCard.__init__(self)
        self.damage = damage
        self.name = "TRAP"

    def turn_card(self,hero):
        AbstractCard.turn_card(self,hero)
        hero.take_damage(self.damage,False)

    # debug
    def debug_print(self):
        print "TRAP: "+str(self.damage)
