from abstractcard import AbstractCard
from ..settings import *
from random import randint,choice

# TODO maybe disable after certain amount of spins?
class SlotsCard(AbstractCard):

    def __init__(self,cost,destroy_chance): 
        AbstractCard.__init__(self)
        self.cost = cost
        self.destroy_chance = destroy_chance
        self.destroyed = False
        self.name = "SLOTS"
        self.actions = {
                        'roll':True,
                    }

    def destroy(self):
        self.destroyed = True

    # actions
    def action(self,action,hero):
        if action == "roll" and self.is_action_enabled("roll"):

            if hero.has_num_core_items('gold',self.cost) and not self.destroyed:

                random_roll = randint(0,99)
                hero.lose_items('gold',self.cost)

                if random_roll > 0 and random_roll <= 39:
                    # 40% nothing
                    pass
                elif random_roll > 39 and random_roll <= 89:
                    # 50% item
                    hero.gain_items(choice(SETTINGS['core_items'].keys()),1)
                else:
                    #10% lose life
                    hero.take_damage(1,True)

                if randint(0,99) <= self.destroy_chance:
                    self.destroyed = True
                    self.disable_action("roll")

    # debug
    def debug_print(self):
        print "SLOTS: "+str(self.cost)+" ("+str(self.destroy_chance)+"%)"
