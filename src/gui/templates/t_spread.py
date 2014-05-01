from abstracttemplate import AbstractTemplate
from ..gui_settings import *
from ..components import *
from ...settings import *

from random import sample

class TSpread(AbstractTemplate):

    def __init__(self,x,y,cards):
        AbstractTemplate.__init__(self,x,y,100,100)
        self.rows = G_SETTINGS['spread_default_rows']
        self.cols = G_SETTINGS['spread_default_cols']
        self.padding = G_SETTINGS['spread_default_padding']
        self._build_spread(cards)

    def _step(self,mousestate):
        AbstractTemplate._step(self,mousestate)

    def _draw(self,screen):
        AbstractTemplate._draw(self,screen)

    def _build_spread(self,cards):

        placements = sample(range(SETTINGS['max_floor_size']),len(cards))

        pos_x,pos_y = self.x,self.y
        count_row,count_col = 0,0
        count_card = 0

        for card in range(SETTINGS['max_floor_size']):

            if count_card in placements:
                self.add_component(CCard(pos_x,pos_y,cards.pop()))
            else:
                self.add_component(CEmptyCard(pos_x,pos_y))

            pos_x += G_SETTINGS['card_w']+self.padding
            count_col += 1

            if(count_col >= self.cols):
                count_col = 0
                pos_x = self.x
                pos_y += G_SETTINGS['card_h']+self.padding

            count_card += 1
