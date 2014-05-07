import sys,pygame
from pygame.locals import *
from settings import *
from random import randint

class Floor():

    def __init__(self,cards):
        self.cards = cards

    def get_size(self):
        return len(self.cards)

    def monsters_remaining(self):
        monster_count = 0
        for card in self.cards:
            if card.name == "MONSTER":
                if card.monster.is_alive():
                    monster_count += 1
        return monster_count

    def visible_monsters_remaining(self):
        monster_count = 0
        for card in self.cards:
            if card.name == "MONSTER":
                if card.monster.is_alive() and card.is_flipped():
                    monster_count += 1
        return monster_count

    # debug
    def debug_print(self):
        for card in self.cards:
            card.debug_print()
