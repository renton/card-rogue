import pygame
from ..gui_settings import *

class AbstractComponent():

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.z = 1
        self.child_components = []
        self.bg_colour = G_SETTINGS['default_component_bg_colour']
        self.hover_bg_colour = G_SETTINGS['default_component_hover_bg_colour']

    def _step(self,mousestate):

        for child in self.child_components:
            child._step(mousestate)

        if pygame.MOUSEBUTTONDOWN in mousestate:
            # left click 
            if 1 in mousestate[pygame.MOUSEBUTTONDOWN]:
                if self.in_bounds(*mousestate[pygame.MOUSEBUTTONDOWN][1]):
                    self.event_click()

    def _draw(self,screen):
        # draw bg colour
        pygame.draw.rect(screen,self.bg_colour,(self.x,self.y,self.w,self.h),0)

        for child in self.child_components:
            child._draw(screen)

    def add_child_component(component):
        self.child_componentsl.append(component)

    def in_bounds(self,x,y):
        return (x >= self.x and x <= (self.x+self.w)) and (y >= self.y and y <= (self.y+self.h))

    # events
    def event_hover(self):
        pass

    def event_click(self):
        pass
