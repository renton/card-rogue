from abstractcard import AbstractCard

class FreeCard(AbstractCard):

    def __init__(self): 
        AbstractCard.__init__(self)

    # debug
    def debug_print(self):
        print "FREE CARD"
