from abstractcomponent import AbstractComponent
from b_text_block import BTextBlock
from ..gui_settings import *
from ...settings import *

class TBattleHud(AbstractComponent):

    def __init__(self,x,y,boardstate):
        AbstractComponent.__init__(self,x,y,0,0)
        self.boardstate = boardstate
        self.hero = boardstate.hero
        self._build_hud()

        self.last_roll = {
                        "base_total":0,
                        "dice":(0,0),
                        "dice_mod":0,
                        "elemental_mod":0,
                        "total":0,
                    }

    def _build_hud(self):
        self.add_child_component(BTextBlock(self.x,self.y,lambda:"BATTLE"))
        self.add_child_component(BTextBlock(self.x,self.y+20,lambda:"HP: "+str(self._get_enemy_hp())))
        self.add_child_component(BTextBlock(self.x,self.y+40,lambda:"FS: "+str(self._get_enemy_fs())))
        self.add_child_component(BTextBlock(self.x,self.y+60,lambda:"OP: "+str(self._get_enemy_op())))
        self.add_child_component(BTextBlock(self.x,self.y+80,lambda:"ATTACK",(0,100,0),100,40,True,lambda:self.attack_action(),True))
        self.add_child_component(BTextBlock(self.x,self.y+140,lambda:"total: "+str(self.last_roll['total'])))
        self.add_child_component(BTextBlock(self.x,self.y+160,lambda:"dice: "+str(self.last_roll['dice'])))
        self.add_child_component(BTextBlock(self.x,self.y+180,lambda:"base: "+str(self.last_roll['base_total'])))
        self.add_child_component(BTextBlock(self.x,self.y+200,lambda:"mod: "+str(self.last_roll['dice_mod'])))
        self.add_child_component(BTextBlock(self.x,self.y+220,lambda:"elemental: "+str(self.last_roll['elemental_mod'])))

    def attack_action(self):
        if self.boardstate.cur_monster_target:
            dice_results = self.boardstate.attack()
            # TODO just return a bloody dict
            if dice_results:
                self.last_roll['total'] = dice_results[0]
                self.last_roll['base_total'] = dice_results[1]
                self.last_roll['dice'] = dice_results[2]
                self.last_roll['dice_mod'] = dice_results[3]
                self.last_roll['elemental_mod'] = dice_results[4]

    def _get_enemy_hp(self):
        if self.boardstate.cur_monster_target:
            return self.boardstate.cur_monster_target.hp
        else:
            return ""
    def _get_enemy_op(self):
        if self.boardstate.cur_monster_target:
            return self.boardstate.cur_monster_target.overpower_roll
        else:
            return ""
    def _get_enemy_fs(self):
        if self.boardstate.cur_monster_target:
            return self.boardstate.cur_monster_target.first_strike_roll
        else:
            return ""
