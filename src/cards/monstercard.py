from abstractcard import AbstractCard

class MonsterCard(AbstractCard):

    def __init__(self,monster,reward): 
        AbstractCard.__init__(self)
        self.monster = monster
        self.reward = {}
        self.name = "MONSTER"
        self.actions = {
                        "kill":True,
                    }

    def action(self,action,hero):
        if action == "kill" and self.is_action_enabled("kill"):
            self.monster.take_damage(9999)    
            self.disable_action("kill")

    # debug
    def debug_print(self):
        print "MONSTER: "+str(self.monster)+" REWARD:"+str(self.reward)
