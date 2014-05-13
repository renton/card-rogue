from abstractcomponent import AbstractComponent
from b_text_block import BTextBlock
from ..gui_settings import *
from ...settings import *

class CCard(AbstractComponent):

    def __init__(self,x,y,card,boardstate):
        AbstractComponent.__init__(
                                    self,
                                    x,
                                    y,
                                    G_SETTINGS['card_w'],
                                    G_SETTINGS['card_h'],
                                )
        self.card = card
        self.bg_colour = G_SETTINGS['card_turned_bg_colour']
        self._init_card()
        self.flipped = False
        self.boardstate = boardstate

    def _step(self,mousestate):
        AbstractComponent._step(self,mousestate)

        for k,v in self.actions.items():
            if not self.card.is_action_enabled(k):
                self.actions[k].bg_colour = (32,32,32)

    def _init_card(self):
        self.label = self.add_child_component(BTextBlock(self.x,self.y,lambda:str(self.card.name),(32,0,0),0,0,False))
        self.actions = {}
        lambda_click_events = {}
    
        # TODO handle multiple actions
        y_offset = 40
        for k,v in self.card.actions.items():
            self.actions[k] = self.add_child_component(BTextBlock(self.x,self.y+y_offset,build_lambda(k),(0,100,0),100,40,False,build_lambda_lambda(k,lambda k:self._action(k))))
            lambda_click_events[k] = lambda:self._action(k)
            y_offset += 60

    def _flip(self):
        if not self.flipped:
            self.boardstate.flip_card(self.card)
            self.label.show()
            for k,v in self.actions.items():
                self.actions[k].show()
            self.bg_colour = (23,44,30)
            self.flipped = True

    def _action(self,action):
        self.boardstate.action_card(self.card,action)

    # events
    def event_click(self):
        self._flip()
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
