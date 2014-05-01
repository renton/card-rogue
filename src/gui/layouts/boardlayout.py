from abstractlayout import AbstractLayout
from ..gui_settings import *

from ..templates import *

class BoardLayout(AbstractLayout):

    def __init__(self):
        AbstractLayout.__init__(self)

        self.add_template(TSpread(
                                    G_SETTINGS['spread_x'],
                                    G_SETTINGS['spread_y']),
                        )

    def _step(self):
        AbstractLayout._step(self)

    def _draw(self,screen):
        AbstractLayout._draw(self,screen)

    def _input(self):
        AbstractLayout._input(self)
