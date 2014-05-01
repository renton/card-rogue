from random import choice
from settings import *

class Dice():
    def __init__(self):
        pass

    def roll(self,num_dice):
        dice_outcome = []
        total = 0
        for i in range(num_dice):
            outcome = choice(SETTINGS['dice_sides'])
            dice_outcome.append(outcome)
            total += outcome

        return (total,dice_outcome)
