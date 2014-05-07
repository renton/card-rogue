from abstractcard import AbstractCard

class ArenaCard(AbstractCard):

    def __init__(self,monsters,reward): 
        AbstractCard.__init__(self)
        self.monsters = monsters
        self.reward = reward
        self.name = "ARENA"
        self.actions = {
                        "enter":True,
                        }

    def get_size(self):
        return len(self.monsters)

    # actions
    def action(self,action,hero):
        if action == "enter" and self.is_action_enabled("enter"):
            self.disable_action("enter")

    # debug
    def debug_print(self):
        print "ARENA: "+str(self.get_size())+" REWARD: "+str(self.reward)
