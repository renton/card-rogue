from abstractcomponent import AbstractComponent
from t_spread import TSpread
from t_hero_hud import THeroHud
from ..gui_settings import *
from ...settings import *

class BoardLayout(AbstractComponent):

    def __init__(self,cards,hero,boardstate):
        AbstractComponent.__init__(
                                    self,
                                    SETTINGS['top_left_x'],
                                    SETTINGS['top_left_y'],
                                    SETTINGS['window_x_size'],
                                    SETTINGS['window_y_size'],
                                    )
        self.cards = cards
        self.hero = hero
        self.board = boardstate
        self.bg_colour = (0,0,0)

    def _setup(self,game):
        self.add_child_component(TSpread(
                                    G_SETTINGS['spread_x'],
                                    G_SETTINGS['spread_y'],
                                    #TODO WRONG what if state changes?
                                    self.cards,
                                    self.board,
                                )
                        )

        self.add_child_component(THeroHud(
                                    G_SETTINGS['hero_hud_x'],
                                    G_SETTINGS['hero_hud_y'],
                                    self.hero,
                                )
                        )
