from ..settings import *

class AbstractHero():

    def __init__(self,hero_string=SETTINGS['default_hero_string']):

        print "loading "+hero_string+" stats"

        self.hero_string = hero_string
        self._load_stats()

    def _load_stats(self):
        stats = SETTINGS['heroes'][self.hero_string]

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
        self.evade_percent = stats['evade_percent']
        self.crit_percent = stats['crit_percent']

        # inventory
        self.items = []

        self.core_items = {}
        for k,v in SETTINGS['core_items'].items():
            self.core_items[k] = stats['start_core_items'][k]

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
        self.cur_hp += amount

        if self.cur_hp > self.max_hp:
            self.cur_hp = self.max_hp

    def level_up(self):
        pass

    def take_damage(self,amount,is_fatal):
        self.cur_hp -= amount
        
        if self.cur_hp <= 0 and not is_fatal:
            self.cur_hp = 1

        if self.cur_hp <= 0:
            self.die()

    def die(self):
        print "ded"

    # events
    def event_after_card_flip(self):
        pass

    def event_after_exit(self):
        pass

    def event_after_damage_to_monster(self):
        pass

    def event_after_monster_kill(self):
        pass
