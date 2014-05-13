import sys,pygame
from pygame.locals import *
from settings import *

from floor import Floor
from cards import *
from monsterfactory import MonsterFactory

from random import randint,choice,sample,shuffle

class FloorFactory():

    def __init__(self):
        self.mf = MonsterFactory()

    def generate_floor(self,floor_lvl):

        self.floor_lvl = floor_lvl
        if self.floor_lvl >= SETTINGS['max_floor_size']:
            self.floor_lvl = SETTINGS['max_floor_size']-1

        cards = []
        cards.append(self._gen_exit_card())

        for i in range(self.floor_lvl):

            randroll = randint(0,99)

            # 5%
            if randroll > 0 and randroll <= 4:
                cards.append(self._gen_free_card())
            # 15%
            elif randroll > 4 and randroll <= 19:
                cards.append(self._gen_loot_card())
            # 10%
            elif randroll > 19 and randroll <= 29:
                cards.append(self._gen_tip_card())
            # 5%
            elif randroll > 29 and randroll <= 34:
                cards.append(self._gen_chest_card())
            # 15%
            elif randroll > 34 and randroll <= 49:
                cards.append(self._gen_trade_card())
            # 10%
            elif randroll > 49 and randroll <= 59:
                cards.append(self._gen_fairy_card())
            # 5%
            elif randroll > 59 and randroll <= 64:
                cards.append(self._gen_slots_card())
            # 20%
            elif randroll > 64 and randroll <= 84:
                cards.append(self._gen_monster_card())
            # 5%
            elif randroll > 84 and randroll <= 89:
                cards.append(self._gen_trap_card())
            # 5%
            elif randroll > 89 and randroll <= 94:
                cards.append(self._gen_arena_card())
            # 5%
            else:
                cards.append(self._gen_thief_card())

        shuffle(cards)

        return Floor(cards)

    # gen card types
    def _gen_free_card(self):
        return FreeCard()

    def _gen_loot_card(self):
        reward_roll = randint(0,99)
        reward = {}

        if reward_roll > 0 and reward_roll <= 9:
            # 200% key
            reward = {'keys':1}
        elif reward_roll > 9 and reward_roll <= 19:
            # 20% wep
            reward = {choice(SETTINGS['ko_weps']):1}
        else:
            # 60% gold
            reward = {'gold':SETTINGS['core_items']['gold']['find_qty']()}

        return LootCard(reward)

    def _gen_tip_card(self):
        return TipCard()

    def _gen_chest_card(self):
        reward_roll = randint(0,99)
        reward = {}

        if reward_roll > 0 and reward_roll <= 9:
            # 200% key
            reward = {'keys':1}
        elif reward_roll > 9 and reward_roll <= 19:
            # 20% wep
            reward = {choice(SETTINGS['ko_weps']):1}
        else:
            # 60% gold
            reward = {'gold':SETTINGS['core_items']['gold']['chest_find_qty']()}

        return ChestCard(reward)

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

    def _gen_exit_card(self):
        return ExitCard()

    def _gen_thief_card(self):

        steal = {choice(SETTINGS['core_items'].keys()):1}

        return ThiefCard(steal)
