from random import randint,choice,sample

SETTINGS = {}

# window
SETTINGS['fullscreen_mode'] = False
SETTINGS['window_x_size'] = 800
SETTINGS['window_y_size'] = 600
SETTINGS['default_fps'] = 60

# board stats
SETTINGS['default_starting_floor'] = 10
SETTINGS['max_floor_size'] = 25

# hero stats
SETTINGS['default_hero_string'] = "default"
SETTINGS['default_start_xp'] = 0
SETTINGS['default_start_lvl'] = 1
SETTINGS['default_next_lvl_xp'] = 1
SETTINGS['default_elemental_attack'] = 0
SETTINGS['default_trade_ratio'] = 3

SETTINGS['heroes'] = {
    'default': {
        'name':'default hero',
        'description':'default description',
        'max_hp':3,
        'dice_modifier':0,
        'evade_percent':0,
        'crit_percent':0,
        'start_core_items':{
            'bows':1,
            'wands':1,
            'swords':1,
            'keys':1,
            'gold':1,
        },
        'elemental_attack':{
        },
    },
    'viking': {
        'name':'viking hero',
        'description':'viking description',
        'max_hp':3,
        'dice_modifier':0,
        'evade_percent':0,
        'crit_percent':0,
        'start_core_items':{
            'bows':1,
            'wands':1,
            'swords':1,
            'keys':1,
            'gold':1,
        },
        'elemental_attack':{
            'fire':2,
        },
    },
    'merchant': {
        'name':'merchant hero',
        'description':'Merchant description',
        'max_hp':3,
        'dice_modifier':-3,
        'evade_percent':0,
        'crit_percent':0,
        'start_core_items':{
            'bows':1,
            'wands':1,
            'swords':1,
            'keys':1,
            'gold':1,
        },
        'elemental_attack':{
        },
        'required_floor_card':'trade',
    },
}

# inventory
SETTINGS['core_items'] = {
    'bows':{
        'chest_find_qty':lambda:randint(2,3),
    },
    'wands':{
        'chest_find_qty':lambda:randint(2,3),
    },
    'swords':{
        'chest_find_qty':lambda:randint(2,3),
    },
    'keys':{
        'chest_find_qty':lambda:randint(2,3),
    },
    'gold':{
        'ratio_trade_multiplier':lambda: randint(1,5),
        'find_qty':lambda: randint(1,10),
        'chest_find_qty':lambda:randint(5,25),
    },
}

# elements
SETTINGS['elements'] = ['fire','ice','electric','earth','dark','holy','plant']

# card types
SETTINGS['card_types'] = {
    'fairy':{
        'help_text':'fairy',
        # TODO this is kinda ghetto
        'hp_gain_qty':lambda:choice([1,1,1,1,2,3]),
        'max_per_floor':2,
    },
    'slots':{
        'cost':lambda:randint(1,5),
        'destroy_chance':lambda:randint(0,20),
        'max_per_floor':3,
        'rewards_probability': {
            'core_item':20,
            'lose_hp':10,
            'item':5,
            'lose':65,
        }
    },
    'trap':{
        'max_per_floor':4,
        'evade_multiplier':2,
        'damage':1,
    },
    'monster':{
    },
    'arena':{
        'max_per_floor':2,
    },
    'chest':{
        'max_per_floor':5,
        'reward_probability': {
            'core_item':60,
            'item':40,
        }
    },
    'loot':{
    },
    'shrine':{
        'max_per_floor':2,
    },
    'tip':{
        'max_per_floor':3,
    },
    'free':{
    },
    'weird':{
        'max_per_floor':1,
    },
    'exit':{
        'required':True,
        'max_per_floor':1,
    },
    'ally':{
        'max_per_floor':3,
    },
    'trade':{
        'ratios':[
                    (1,1),
                    (2,1),
                    (3,1),
                    (3,2),
                    (4,1),
                    (5,1),
                    (5,2),
                ],
    },
    'bloodtrade':{
        'cost':lambda:randint(1,3),
        'find_multiplier':lambda:randint(1,2),
        'ratios':[
                    (1,1),
                    (2,1),
                    (3,1),
                    (3,2),
                    (4,1),
                ],
    }
}

# advice tips
# TODO move this to file reader
SETTINGS['advice_tips'] = [
    'sample tip',
    'another sample tip',
    'yet another sample tip',
]

# dice
SETTINGS['dice_sides'] = [1,2,3,4,5,6]
