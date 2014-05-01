from abstractcard import AbstractCard
from ..settings import *

class FairyCard(AbstractCard):

    def __init__(self,hp_gain): 
        AbstractCard.__init__(self)
        self.used = False
        self.hp_gain = hp_gain

    # actions
    def action_use(self):
        self.used = True

    # debug
    def debug_print(self):
        print "FAIRY: "+str(self.hp_gain)

