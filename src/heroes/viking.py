from ..settings import *
from abstracthero import AbstractHero

class VikingHero(AbstractHero):

    def __init__(self):
        AbstractHero.__init__(self,"viking")
