from abstractcard import AbstractCard
from ..settings import *

class TrapCard(AbstractCard):
    # TODO trap can't kill you. can only take you down to 1 hp

    def __init__(self,damage): 
        AbstractCard.__init__(self)
        self.damage = damage

    # debug
    def debug_print(self):
        print "TRAP: "+str(self.damage)
