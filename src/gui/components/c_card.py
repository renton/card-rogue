from abstractcomponent import AbstractComponent
from ..gui_settings import *

class CCard(AbstractComponent):

    def __init__(self,x,y,card):
        AbstractComponent.__init__(
                                    self,
                                    x,
                                    y,
                                    G_SETTINGS['card_w'],
                                    G_SETTINGS['card_h'],
                                )
        self.card = card
        self.bg_colour = G_SETTINGS['card_turned_bg_colour']

    def _step(self,mousestate):
        AbstractComponent._step(self,mousestate)

    def _draw(self,screen):
        AbstractComponent._draw(self,screen)

    def event_click(self):
        self.card.debug_print()

class CEmptyCard(AbstractComponent):

    def __init__(self,x,y):
        AbstractComponent.__init__(
                                    self,
                                    x,
                                    y,
                                    G_SETTINGS['card_w'],
                                    G_SETTINGS['card_h'],
                                )

    def _step(self,mousestate):
        AbstractComponent._step(self,mousestate)

    def _draw(self,screen):
        AbstractComponent._draw(self,screen)
