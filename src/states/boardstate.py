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

        # monster target
        self.cur_monster_target = None

    def _generate_floor(self):
        self.cur_floor = self.ff.generate_floor(self.cur_floor_lvl)
        self.set_signal("new_floor")

    def get_floor(self):
        return self.cur_floor

    def _step(self):
        self.ticks += 1

    def _input(self,im):
        State._input(self,im)

    def target_monster(self,monster):
        self.cur_monster_target = monster

    def attack(self):
        if self.cur_monster_target and self.cur_monster_target.alive:
            base_total,roll = self.dice.roll(self.hero.num_dice_roll)

            roll_mod = self.hero.get_roll_modifiers(self.cur_monster_target)
            element_mod = self.hero.get_elemental_modifiers(self.cur_monster_target)

            total = base_total+roll_mod+element_mod

            if total >= self.cur_monster_target.overpower_roll:
                self.cur_monster_target.take_damage(total)
            else:
                if self.hero.always_first_strike or total >= self.cur_monster_target.first_strike_roll:
                    # first strike
                    self.cur_monster_target.take_damage(total)

                    # monster counter
                    if self.cur_monster_target.alive:
                        self.hero.take_damage(self.cur_monster_target.dmg)
                else:
                    # monster strike
                    self.hero.take_damage(self.cur_monster_target.dmg)

                    # hero counter
                    if self.hero.alive:
                        self.cur_monster_target.take_damage(total)
                    else:
                        self._game_over()

            if not self.cur_monster_target.alive:
                self.hero.gain_xp(1)

            return (total,base_total,roll,roll_mod,element_mod)
        else:
            return False

    def ko(self):
        if self.cur_monster_target.alive:
            for k,v in self.cur_monster_target.ko_items.items():
                if not self.hero.has_num_core_items(k,v):
                    return False

            monster.ko_damage()

            for k,v in monster.ko_items.items():
                hero.lose_items(k,v)

            return True


    def _game_over(self):
        print "game over"

    # actions
    # TODO - kind of weird to pass card, but keeps gui cleaner
    def flip_card(self,card):
        card.turn_card(self.hero)

    def action_card(self,card,action):

        # TODO this is hacky... must be a cleaner way
        if card.name == "MONSTER" and action == "fight":
            self.target_monster(card.monster)

        if card.action(action,self.hero) == True:
            self._exit_floor()

    def _exit_floor(self):
        if self.cur_floor.visible_monsters_remaining() <= 0:
            self.cur_floor_lvl += 1
            self._generate_floor()

    def _advance_floor(self):
        self.cur_floor_lvl += 1
        self._generate_floor()
