from abstractcard import AbstractCard
from ..settings import *

class TradeCard(AbstractCard):

    def __init__(self,need,gain): 
        AbstractCard.__init__(self)
        self.need = need
        self.gain = gain
        self.name = "TRADE"
        self.actions = {
                        "trade":True,
                    }

    # actions
    def action(self,action,hero):
        if action == "trade" and self.is_action_enabled("trade") and self.can_trade(hero):
            for k,v in self.need.items():
                hero.lose_items(k,v)
            for k,v in self.gain.items():
                hero.gain_items(k,v)

    def can_trade(self,hero):
        for k,v in self.need.items():
            if not hero.has_num_core_items(k,v):
                return False
        return True

    # debug
    def debug_print(self):
        print "TRADE: "+str(self.need)+" => "+str(self.gain)
