from abstractcomponent import AbstractComponent
from b_text_block import BTextBlock
from ..gui_settings import *
from ...settings import *

class TDungeonHud(AbstractComponent):

    def __init__(self,x,y,boardstate):
        AbstractComponent.__init__(self,x,y,0,0)
        self.boardstate = boardstate
        self._build_hud()

    def _build_hud(self):
        self.add_child_component(BTextBlock(self.x,self.y,lambda:"FLOOR: "+str(self.boardstate.cur_floor_lvl)))
        self.add_child_component(BTextBlock(self.x+200,self.y,lambda:"monsters: "+str(self.boardstate.cur_floor.monsters_remaining())))
        self.add_child_component(BTextBlock(self.x+200,self.y+20,lambda:"visible: "+str(self.boardstate.cur_floor.visible_monsters_remaining())))
