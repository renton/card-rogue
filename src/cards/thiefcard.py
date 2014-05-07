from abstractcard import AbstractCard

class ThiefCard(AbstractCard):

    def __init__(self,steal): 
        AbstractCard.__init__(self)
        self.steal = steal
        self.name = "THIEF"

    def turn_card(self,hero):
        AbstractCard.turn_card(self,hero)

        for k,v in self.steal.items():
            hero.lose_items(k,v)

    # debug
    def debug_print(self):
        print "THIEF: "+str(self.steal)
