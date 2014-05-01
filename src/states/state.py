import sys,pygame
from pygame.locals import *

class State():

    def __init__(self,screen,rm):
        self.screen = screen
        self.rm = rm

        self.last_keystate = {}

    def _draw(self):
        pass

    def _step(self):
        pass

    def _input(self,im):

        # key input handling
        if im.keystate[K_ESCAPE]:
            pygame.display.quit()
            sys.exit()
