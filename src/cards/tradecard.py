from abstractcard import AbstractCard
from ..settings import *

class TradeCard(AbstractCard):

    def __init__(self,need,gain): 
        AbstractCard.__init__(self)
        self.need = need
        self.gain = gain
        self.name = "TRADE"

    # actions
    def action_make_trade(self):
        pass

    # debug
    def debug_print(self):
        print "TRADE: "+str(self.need)+" => "+str(self.gain)
