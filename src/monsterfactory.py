import sys,pygame
from pygame.locals import *
from settings import *

from monster import Monster
from random import randint,choice,sample
from dice import Dice

class MonsterFactory():

    def __init__(self):
        pass

    def generate_monster(self,floor_lvl):

        # TODO REFACTOR + CLEANUP

        dice = Dice()

        if floor_lvl > 100:
            floor_lvl = 100

        # hp
        hp_num_dice = 1
        hp_num_extra_dice = 4
        total_hp = 0
        for i in range(hp_num_dice):
            total_hp += dice.roll(1)[0]
        for i in range(hp_num_extra_dice):
            if randint(1,100) <= floor_lvl:
                total_hp += dice.roll(1)[0]

        # fs + op
        fs = randint(2,12)
        op = fs+randint(1,5)
        if op > 12:
            op = 12

        # ko
        ko_weps = ['bows','wands','swords'] 
        ko_num_dice = 1
        ko_num_extra_dice = 5
        ko = {}
        for i in range(ko_num_dice):
            wep = choice(ko_weps)
            if wep not in ko:
                ko[wep] = 0
            ko[wep] += 1
        for i in range(ko_num_extra_dice):
            if randint(1,100) <= floor_lvl:
                wep = choice(ko_weps)
                if wep not in ko:
                    ko[wep] = 0
                ko[wep] += 1

        # reward
        reward_roll = randint(0,99)
        reward = {}

        if reward_roll > 0 and reward_roll <= 9:
            # 10% key
            reward = {'keys':1}
        elif reward_roll > 9 and reward_roll <= 19:
            reward = {choice(ko_weps):1}
            # 10% wep
        elif reward_roll > 19 and reward_roll <= 49:
            # 30% nothing
            reward = {}
        else:
            # 50% gold
            reward = {'gold':SETTINGS['core_items']['gold']['find_qty']()}

        return Monster(total_hp,fs,op,ko,reward)
