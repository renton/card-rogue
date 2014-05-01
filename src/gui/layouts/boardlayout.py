from abstractlayout import AbstractLayout
from ..gui_settings import *

from ..templates import *

class BoardLayout(AbstractLayout):

    def __init__(self):
        AbstractLayout.__init__(self)



    def _step(self,mousestate):
        AbstractLayout._step(self,mousestate)

    def _draw(self,screen):
        AbstractLayout._draw(self,screen)

    def _setup(self,game):
        self.add_template(TSpread(
                                    G_SETTINGS['spread_x'],
                                    G_SETTINGS['spread_y'],
                                    #TODO WRONG what if state changes?
                                    game.cur_state.cur_floor.cards,
                                )
                        )
