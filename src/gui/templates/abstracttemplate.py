from ..gui_settings import *
import pygame

# TODO templates, components + layouts can all either be the same (with children) or all extend a base drawabale)
class AbstractTemplate():

    def __init__(self,x,y,w,h):
        self.components = []
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bg_colour = G_SETTINGS['default_template_bg_colour']

    def _step(self,mousestate):
        for component in self.components:
            component._step(mousestate)

    def _draw(self,screen):
        # draw bg colour
        pygame.draw.rect(screen,self.bg_colour,(self.x,self.y,self.w,self.h),0)

        for component in self.components:
            component._draw(screen)

    def _setup(self):
        pass

    def add_component(self,component):
        self.components.append(component)
