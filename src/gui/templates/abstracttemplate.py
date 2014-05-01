from ..gui_settings import *
import pygame

class AbstractTemplate():

    def __init__(self,x,y,w,h):
        self.components = []
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bg_colour = G_SETTINGS['default_template_bg_colour']

    def _step(self):
        for component in self.components:
            component._step()

    def _draw(self,screen):
        # draw bg colour
        pygame.draw.rect(screen,self.bg_colour,(self.x,self.y,self.w,self.h),0)

        for component in self.components:
            component._draw(screen)
