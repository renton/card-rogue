import sys,pygame
from pygame.locals import *
from settings import *

from floor import Floor
from cards import *
from monsterfactory import MonsterFactory

from random import randint,choice,sample

class FloorFactory():

    def __init__(self):
        self.mf = MonsterFactory()

    def generate_floor(self,floor_lvl):

        self.floor_lvl = floor_lvl
        if self.floor_lvl > SETTINGS['max_floor_size']:
            self.floor_lvl = SETTINGS['max_floor_size']

        cards = []
        for i in range(floor_lvl):

            test = randint(0,9)
            #test = 4

            if test == 0:
                cards.append(self._gen_free_card())

            if test == 1:
                cards.append(self._gen_loot_card())

            if test == 2:
                cards.append(self._gen_tip_card())

            if test == 3:
                cards.append(self._gen_chest_card())

            if test == 4:
                cards.append(self._gen_trade_card())

            if test == 5:
                cards.append(self._gen_fairy_card())

            if test == 6:
                cards.append(self._gen_slots_card())

            if test == 7:
                cards.append(self._gen_monster_card())

            if test == 8:
                cards.append(self._gen_trap_card())

            if test == 9:
                cards.append(self._gen_arena_card())

        return Floor(cards)

    # gen card types
    def _gen_free_card(self):
        return FreeCard()

    def _gen_loot_card(self):
        return LootCard({"bows":1})

    def _gen_tip_card(self):
        return TipCard()

    def _gen_chest_card(self):
        return ChestCard({"wands":1})

    def _gen_trade_card(self):
        need_ratio,gain_ratio = choice(SETTINGS['card_types']['trade']['ratios'])
        items = sample(SETTINGS['core_items'].keys(),2)
        need_item,gain_item = items[0],items[1]

        if 'ratio_trade_multiplier' in SETTINGS['core_items'][need_item]:
            need_ratio *= SETTINGS['core_items'][need_item]['ratio_trade_multiplier']()

        # TODO can this cause infinite gain trading?
        if 'ratio_trade_multiplier' in SETTINGS['core_items'][gain_item]:
            gain_ratio *= SETTINGS['core_items'][gain_item]['ratio_trade_multiplier']()

        return TradeCard({need_item:need_ratio},{gain_item:gain_ratio})

    def _gen_fairy_card(self):
        return FairyCard(SETTINGS['card_types']['fairy']['hp_gain_qty']())

    def _gen_slots_card(self):
        return SlotsCard(SETTINGS['card_types']['slots']['cost'](),SETTINGS['card_types']['slots']['destroy_chance']())

    def _gen_monster_card(self):
        return MonsterCard(self.mf.generate_monster(self.floor_lvl),{"wands":1})

    def _gen_trap_card(self):
        return TrapCard(SETTINGS['card_types']['trap']['damage'])

    def _gen_arena_card(self):
        # TODO better reward for more monsters
        return ArenaCard([self.mf.generate_monster(self.floor_lvl)],{"wands":1})
