from abstractcard import AbstractCard

class ChestCard(AbstractCard):
    #TODO chest can also have certain core_items in higher qty

    def __init__(self,reward): 
        AbstractCard.__init__(self)
        self.locked = True
        self.reward = reward
        self.name = "CHEST"
        self.actions = {
                            "loot":True,
                        }

    # actions
    def action(self,action,hero):
        if action=="loot" and self.is_action_enabled("loot"):
            temp = self.reward
            self.reward = {}
            self.disable_action("loot")

    # debug
    def debug_print(self):
        print "CHEST: "+str(self.reward)
