from abstractcard import AbstractCard

class MonsterCard(AbstractCard):

    def __init__(self,monster,reward): 
        AbstractCard.__init__(self)
        self.monster = monster
        self.reward = {}
        self.name = "MONSTER"
        self.actions = {
                        "fight":True,
                        "ko":True,
                    }

    def action(self,action,hero):
        if action == "fight" and self.is_action_enabled("fight"):
            pass
        if action == "ko" and self.is_action_enabled("ko"):
            pass

        if self.monster.alive == False:
            self.disable_action("fight")
            self.disable_action("ko")

    def is_action_enabled(self,action):
        return self.monster.alive

    # debug
    def debug_print(self):
        print "MONSTER: "+str(self.monster)+" REWARD:"+str(self.reward)
