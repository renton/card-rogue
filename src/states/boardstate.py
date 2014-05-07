import pygame
from pygame.locals import *
from state import State
from ..settings import *

from ..floorfactory import FloorFactory
from ..dice import Dice
from ..heroes import VikingHero

# gui
from ..gui import PGui

class BoardState(State):

    def __init__(self,screen,rm):
        State.__init__(self,screen,rm)

        # board stats
        self.cur_floor_lvl = SETTINGS['default_starting_floor']

        # dice
        self.dice = Dice()

        # floor
        self.ff = FloorFactory()
        self._generate_floor()

        # timer
        self.ticks = 0

        # hero
        self.hero = VikingHero()

    def _generate_floor(self):
        self.cur_floor = self.ff.generate_floor(self.cur_floor_lvl)
        self.set_signal("new_floor")

    def get_floor(self):
        return self.cur_floor

    def _step(self):
        self.ticks += 1

    def _input(self,im):
        State._input(self,im)

    # actions
    # TODO - kind of weird to pass card, but keeps gui cleaner
    def flip_card(self,card):
        card.turn_card(self.hero)

    def action_card(self,card,action):
        if card.action(action,self.hero) == True:
            self._exit_floor()

    def _exit_floor(self):
        if self.cur_floor.visible_monsters_remaining() <= 0:
            self.cur_floor_lvl += 1
            self._generate_floor()

    def _advance_floor(self):
        self.cur_floor_lvl += 1
        self._generate_floor()
