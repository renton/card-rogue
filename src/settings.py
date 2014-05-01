
SETTINGS = {}

# window
SETTINGS['fullscreen_mode'] = False
SETTINGS['window_x_size'] = 800
SETTINGS['window_y_size'] = 600
SETTINGS['default_fps'] = 60

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
}

# inventory
SETTINGS['core_items'] = ['bows','wands','swords','keys','gold']

# elements
SETTINGS['elements'] = ['fire','ice','electric','earth','dark','holy','plant']
