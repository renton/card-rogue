from abstractcard import AbstractCard
from ..settings import *

from random import choice

class TipCard(AbstractCard):

    def __init__(self): 
        AbstractCard.__init__(self)
        self.tip_text = choice(SETTINGS['advice_tips'])

    # actions
    def action_get_tip(self):
        return self.tip_text

    # debug
    def debug_print(self):
        print "TIP: "+str(self.action_get_tip())
