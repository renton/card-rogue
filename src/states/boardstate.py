import pygame
from pygame.locals import *
from state import State
from ..settings import *

from ..floorfactory import FloorFactory

from ..heroes import VikingHero

class BoardState(State):

    def __init__(self,screen,rm):
        State.__init__(self,screen,rm)

        # board stats
        self.cur_floor = 1

        # floor
        self.ff = FloorFactory()
        self.cur_floor = None

        # timer
        self.ticks = 0

        # hero
        self.hero = VikingHero()

    def _step(self):
        self.ticks += 1

    def _input(self,im):
        State._input(self,im)

    def _draw(self):
        pass
