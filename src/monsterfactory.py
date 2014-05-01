import sys,pygame
from pygame.locals import *
from settings import *

from monster import Monster
from random import randint,choice,sample

class MonsterFactory():

    def __init__(self):
        pass

    def generate_monster(self,floor_lvl):
        return Monster()
