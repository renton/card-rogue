from abstracttemplate import AbstractTemplate
from ..gui_settings import *

class TSpread(AbstractTemplate):

    def __init__(self,x,y):
        AbstractTemplate.__init__(self,x,y,100,100)
        self.rows = G_SETTINGS['spread_default_rows']
        self.cols = G_SETTINGS['spread_default_cols']
        self.padding = G_SETTINGS['spread_default_padding']

    def _step(self):
        AbstractTemplate._step(self)

    def _draw(self,screen):
        AbstractTemplate._draw(self,screen)
