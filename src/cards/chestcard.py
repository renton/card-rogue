from abstractcard import AbstractCard

class ChestCard(AbstractCard):
    #TODO chest can also have certain core_items in higher qty

    def __init__(self,reward): 
        AbstractCard.__init__(self)
        self.locked = True
        self.reward = reward
        self.name = "CHEST"
        self.actions = {
                            "loot":{
                                "fn":lambda hero:self.action_get_reward(hero),
                                "enabled":True,
                            }
                        }

    # actions
    def action_get_reward(self,hero):
        if self.is_action_enabled("loot"):
            temp = self.reward
            self.reward = {}
            self.disable_action("loot")

    # debug
    def debug_print(self):
        print "CHEST: "+str(self.reward)
