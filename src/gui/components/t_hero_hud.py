from abstractcomponent import AbstractComponent
from b_text_block import BTextBlock
from ..gui_settings import *
from ...settings import *

class THeroHud(AbstractComponent):

    def __init__(self,x,y,hero):
        AbstractComponent.__init__(self,x,y,100,1000)
        self.hero = hero
        self._build_hud()

    def _build_hud(self):
        self.add_child_component(BTextBlock(0,0,lambda:str(self.hero.hero_string)))
        self.add_child_component(BTextBlock(0,20,lambda:"LVL: "+str(self.hero.cur_lvl)))
        self.add_child_component(BTextBlock(0,40,lambda:"XP: "+str(self.hero.cur_xp)+" / "+str(self.hero.next_lvl_xp)))
        self.add_child_component(BTextBlock(0,60,lambda:"HP: "+str(self.hero.cur_hp)+" / "+str(self.hero.max_hp)))
        self.add_child_component(BTextBlock(0,80,lambda:"Dice: "+str(self.hero.dice_modifier)))
        self.add_child_component(BTextBlock(0,100,lambda:"Evade%: "+str(self.hero.evade_percent)+"%"))
        self.add_child_component(BTextBlock(0,120,lambda:"Crit%: "+str(self.hero.crit_percent)+"%"))
        self.add_child_component(BTextBlock(0,140,lambda:"Swords: "+str(self.hero.core_items['swords'])))
        self.add_child_component(BTextBlock(0,160,lambda:"Wands: "+str(self.hero.core_items['wands'])))
        self.add_child_component(BTextBlock(0,180,lambda:"Bows: "+str(self.hero.core_items['bows'])))
        self.add_child_component(BTextBlock(0,200,lambda:"Gold: "+str(self.hero.core_items['gold'])))
        self.add_child_component(BTextBlock(0,220,lambda:"Keys: "+str(self.hero.core_items['keys'])))
