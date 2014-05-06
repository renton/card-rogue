from abstractcomponent import AbstractComponent
from b_text_block import BTextBlock
from ..gui_settings import *

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
            if not self.card.actions[k]['enabled']:
                self.actions[k].bg_colour = (32,32,32)

    def _init_card(self):
        self.label = self.add_child_component(BTextBlock(self.x,self.y,lambda:str(self.card.name),(32,0,0),0,0,False))
        self.actions = {}
    
        # TODO handle multiple actions
        for k,v in self.card.actions.items():
            self.actions[k] = self.add_child_component(BTextBlock(self.x,self.y+40,lambda:k,(0,100,0),100,40,False,lambda:self._action(k)))

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
