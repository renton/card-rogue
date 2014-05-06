from abstractcard import AbstractCard

class LootCard(AbstractCard):
    # TODO loot and chest can be the same

    def __init__(self,reward): 
        AbstractCard.__init__(self)
        self.reward = reward
        self.name = "LOOT"
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
        print "LOOT: "+str(self.reward)
