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
            can_ko = True
            if self.monster.alive:
                for k,v in self.monster.ko_items.items():
                    if not hero.has_num_core_items(k,v):
                        can_ko = False

                if can_ko:
                    self.monster.ko_damage()
                    for k,v in self.monster.ko_items.items():
                        hero.lose_items(k,v)

        if self.monster.alive == False:
            self.disable_action("fight")
            self.disable_action("ko")

    def is_action_enabled(self,action):
        return self.monster.alive

    # debug
    def debug_print(self):
        print "MONSTER: "+str(self.monster)
