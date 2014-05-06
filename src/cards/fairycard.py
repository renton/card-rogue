from abstractcard import AbstractCard
from ..settings import *

class FairyCard(AbstractCard):

    def __init__(self,hp_gain): 
        AbstractCard.__init__(self)
        self.hp_gain = hp_gain
        self.name = "FAIRY"
        self.actions = {
                            "catch":{
                                "fn":lambda hero:self.action(hero),
                                "enabled":True,
                            }
                        }
                    
    # actions
    def action(self,hero):
        if self.actions['catch']['enabled']:
            hero.gain_hp(self.hp_gain)
            self.disable_action("catch")

    # debug
    def debug_print(self):
        #print "FAIRY: "+str(self.hp_gain)
        pass

