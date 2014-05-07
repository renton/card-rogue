from abstractcard import AbstractCard
from ..settings import *

class ExitCard(AbstractCard):
    # TODO trap can't kill you. can only take you down to 1 hp

    def __init__(self): 
        AbstractCard.__init__(self)
        self.name = "EXIT"
        self.actions = {
                            "exit":True,
                        }

    def action(self,action,hero):
        if action == "exit":
            return True

    # debug
    def debug_print(self):
        print "EXIT"
