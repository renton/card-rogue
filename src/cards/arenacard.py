from abstractcard import AbstractCard

class ArenaCard(AbstractCard):

    def __init__(self,monsters,reward): 
        AbstractCard.__init__(self)
        self.monsters = monsters
        self.reward = reward

    def get_size(self):
        return len(self.monsters)

    # debug
    def debug_print(self):
        print "ARENA: "+str(self.get_size())+" REWARD: "+str(self.reward)
