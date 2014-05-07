import sys,pygame
from pygame.locals import *

class State():

    def __init__(self,screen,rm):
        self.screen = screen
        self.rm = rm

        self.last_keystate = {}

        self.gui_signals = {}

    def _draw(self):
        pass

    def _step(self):
        pass

    def _input(self,im):

        # key input handling
        if im.keystate[K_ESCAPE]:
            pygame.display.quit()
            sys.exit()

    def is_signal(self,signal):
        return signal in self.gui_signals and self.gui_signals[signal]

    def set_signal(self,signal):
        self.gui_signals[signal] = True

    def reset_signal(self,signal):
        if signal in self.gui_signals:
            self.gui_signals[signal] = False
