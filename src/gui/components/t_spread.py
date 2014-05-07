from abstractcomponent import AbstractComponent
from c_card import CCard,CEmptyCard
from ..gui_settings import *
from ...settings import *
from random import sample

class TSpread(AbstractComponent):

    def __init__(self,x,y,cards,boardstate):
        AbstractComponent.__init__(self,x,y,0,0)
        self.rows = G_SETTINGS['spread_default_rows']
        self.cols = G_SETTINGS['spread_default_cols']
        self.padding = G_SETTINGS['spread_default_padding']
        self.boardstate = boardstate
        self.display = False

    def _build_spread(self,cards):

        self.clear_children()

        placements = sample(range(SETTINGS['max_floor_size']),len(cards))

        pos_x,pos_y = self.x,self.y
        count_row,count_col = 0,0
        count_card = 0
        use_card = 0

        for card in range(SETTINGS['max_floor_size']):

            if count_card in placements:
                self.add_child_component(CCard(pos_x,pos_y,cards[use_card],self.boardstate))
                use_card += 1
            else:
                self.add_child_component(CEmptyCard(pos_x,pos_y))

            pos_x += G_SETTINGS['card_w']+self.padding
            count_col += 1

            if(count_col >= self.cols):
                count_col = 0
                pos_x = self.x
                pos_y += G_SETTINGS['card_h']+self.padding

            count_card += 1
