from ..settings import *

class AbstractHero():

    def __init__(self,hero_string=SETTINGS['default_hero_string']):

        print "loading "+hero_string+" stats"

        self.hero_string = hero_string
        self._load_stats()

    def _load_stats(self):
        stats = SETTINGS['heroes'][self.hero_string]


        self.alive = True

        # hp
        self.max_hp = stats['max_hp']
        self.cur_hp = self.max_hp

        # xp
        self.cur_xp = SETTINGS['default_start_xp']
        self.cur_lvl = SETTINGS['default_start_lvl']
        self.next_lvl_xp = SETTINGS['default_next_lvl_xp']

        # dice
        self.dice_modifier = stats['dice_modifier']
        self.num_dice_roll = 2

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

        # traits
        self.always_first_strike = False

    def has_num_core_items(self,core_item,amount):
        return self.core_items[core_item] >= amount

    def lose_items(self,core_item,amount):
        self.core_items[core_item] -= amount
        if self.core_items[core_item] < 0:
            self.core_items[core_item] = 0

    def gain_items(self,core_item,amount):
        self.core_items[core_item] += amount

    def gain_xp(self,amount):
        self.cur_xp += 1

        if self.cur_xp >= self.next_lvl_xp:
            self.level_up()

        if (amount-1) > 0:
            self.gain_xp(amount-1)

    def gain_hp(self,amount):
        self.cur_hp += amount

        if self.cur_hp > self.max_hp:
            self.cur_hp = self.max_hp

    def level_up(self):
        self.cur_hp = self.max_hp
        self.cur_xp = 0
        self.cur_lvl += 1
        self.next_lvl_xp += 1

    def take_damage(self,amount,is_fatal=True):
        self.cur_hp -= amount
        
        if self.cur_hp <= 0 and not is_fatal:
            self.cur_hp = 1

        if self.cur_hp <= 0:
            self.die()

    def die(self):
        self.alive = False

    def get_roll_modifiers(self,monster):
        return 0

    def get_elemental_modifiers(self,monster):
        return 0

    # events
    def event_after_card_flip(self):
        pass

    def event_after_exit(self):
        pass

    def event_after_damage_to_monster(self):
        pass

    def event_after_monster_kill(self):
        pass
