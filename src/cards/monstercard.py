from abstractcard import AbstractCard

class MonsterCard(AbstractCard):

    def __init__(self,monster,reward): 
        AbstractCard.__init__(self)
        self.monster = monster
        self.reward = {}

    # debug
    def debug_print(self):
        print "MONSTER: "+str(self.monster)+" REWARD:"+str(self.reward)
