from abstractcard import AbstractCard
from ..settings import *

# TODO maybe disable after certain amount of spins?
class SlotsCard(AbstractCard):

    def __init__(self,cost,destroy_chance): 
        AbstractCard.__init__(self)
        self.cost = cost
        self.destroy_chance = destroy_chance
        self.destroyed = False

    def destroy(self):
        self.destroyed = True

    # actions
    def action_play(self):
        pass

    # debug
    def debug_print(self):
        print "SLOTS: "+str(self.cost)+" ("+str(self.destroy_chance)+"%)"
