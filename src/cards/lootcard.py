from abstractcard import AbstractCard

class LootCard(AbstractCard):

    def __init__(self,reward): 
        AbstractCard.__init__(self)
        self.reward = reward

    def turn_card(self):
        AbstractCard.turn_card(self)
        pass

    # actions
    def action_get_reward(self):
        temp = self.reward
        self.reward = {}
        return temp

    # debug
    def debug_print(self):
        print "LOOT: "+str(self.reward)
