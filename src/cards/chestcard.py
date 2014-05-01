from abstractcard import AbstractCard

class ChestCard(AbstractCard):
    #TODO chest can also have certain core_items in higher qty

    def __init__(self,reward): 
        AbstractCard.__init__(self)
        self.locked = True
        self.reward = reward

    # actions
    def action_get_reward(self):
        temp = self.reward
        self.reward = {}
        return temp

    # debug
    def debug_print(self):
        print "CHEST: "+str(self.reward)
