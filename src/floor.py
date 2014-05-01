import sys,pygame
from pygame.locals import *
from settings import *

class Floor():

    def __init__(self,cards):
        self.cards = cards

    def get_size(self):
        return len(self.cards)

    # debug
    def debug_print(self):
        for card in self.cards:
            card.debug_print()
