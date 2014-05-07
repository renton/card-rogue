from abstractcard import AbstractCard

class LootCard(AbstractCard):
    # TODO loot and chest can be the same

    def __init__(self,reward): 
        AbstractCard.__init__(self)
        self.reward = reward
        self.name = "LOOT"
        self.actions = {
                            "loot":True,
                        }

    # actions
    def action(self,action,hero):
        if action == "loot" and self.is_action_enabled("loot"):
            temp = self.reward
            for k,v in self.reward.items():
                hero.core_items[k] += v
            self.reward = {}
            self.disable_action("loot")

    # debug
    def debug_print(self):
        print "LOOT: "+str(self.reward)
