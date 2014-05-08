from abstractcomponent import AbstractComponent
from t_spread import TSpread
from t_hero_hud import THeroHud
from t_dungeon_hud import TDungeonHud
from t_battle_hud import TBattleHud
from ..gui_settings import *
from ...settings import *

class BoardLayout(AbstractComponent):

    def __init__(self,game):
        AbstractComponent.__init__(
                                    self,
                                    SETTINGS['top_left_x'],
                                    SETTINGS['top_left_y'],
                                    SETTINGS['window_x_size'],
                                    SETTINGS['window_y_size'],
                                    )
        self.bg_colour = (0,0,0)
        self.t_spread = None
        self.t_hero_hud = None
        self._setup(game)

    def _step(self,mousestate,game):
        AbstractComponent._step(self,mousestate)

        if game.cur_state.is_signal("new_floor"):
            self._new_spread(game)
            game.cur_state.reset_signal("new_floor")

    def _new_spread(self,game):

        if self.t_spread == None:
            self.t_spread = self.add_child_component(TSpread(
                                        G_SETTINGS['spread_x'],
                                        G_SETTINGS['spread_y'],
                                        #TODO WRONG what if state changes?
                                        game.cur_state.cur_floor.cards,
                                        game.cur_state,
                                    )
                            )

        self.t_spread._build_spread(game.cur_state.cur_floor.cards)
        

    def _setup(self,game):
        if self.t_hero_hud:
            del self.t_hero_hud

        self.t_hero_hud = self.add_child_component(THeroHud(
                                    G_SETTINGS['hero_hud_x'],
                                    G_SETTINGS['hero_hud_y'],
                                    game.cur_state.hero,
                                )
                        )

        self.t_dungeon_hud = self.add_child_component(TDungeonHud(
                                    400,
                                    10,
                                    game.cur_state,
                                )
                        )

        self.t_battle_hud = self.add_child_component(TBattleHud(
                                    1000,
                                    10,
                                    game.cur_state,
                                )
                        )


