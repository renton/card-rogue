from ..settings import *

class AbstractHero():

    def __init__(self,hero_string=SETTINGS['default_hero_string']):

        print "loading "+hero_string+" stats"

        stats = SETTINGS['heroes'][hero_string]

        # hp
        self.max_hp = stats['max_hp']
        self.cur_hp = self.max_hp

        # xp
        self.cur_xp = SETTINGS['default_start_xp']
        self.cur_lvl = SETTINGS['default_start_lvl']
        self.next_lvl_xp = SETTINGS['default_next_lvl_xp']

        # dice
        self.dice_modifier = stats['dice_modifier']

        # evade/crit
        self.evace_percent = stats['evade_percent']
        self.crit_percent = stats['crit_percent']

        # inventory
        self.items = []

        self.core_items = {}
        for core_item in SETTINGS['core_items']:
            self.core_items[core_item] = stats['start_core_items'][core_item]

        # trading
        self.trade_ratio = SETTINGS['default_trade_ratio']

        # elemental
        self.elemental_attack = {}
        for element in SETTINGS['elements']:
            if element in stats['elemental_attack']:
                self.elemental_attack[element] = stats['elemental_attack'][element]
            else:
                self.elemental_attack[element] = SETTINGS['default_elemental_attack']

    def gain_xp(self,amount):
        pass

    def gain_hp(self,amount):
        pass

    def level_up(self):
        pass

    def take_damage(self,amount):
        pass

    def die(self):
        pass

    # events
    def event_after_card_flip(self):
        pass

    def event_after_exit(self):
        pass

    def event_after_take_damage(self):
        pass

    def event_after_damage_to_monster(self):
        pass

    def event_after_monster_kill(self):
        pass
