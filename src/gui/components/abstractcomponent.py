import pygame
from ..gui_settings import *

class AbstractComponent():

    def __init__(
                    self,
                    x,
                    y,
                    w,
                    h,
                    click_event=lambda:True,
                    hover_event=lambda:True,
                ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.z = 1
        self.child_components = []
        self.bg_colour = G_SETTINGS['default_component_bg_colour']
        self.hover_bg_colour = G_SETTINGS['default_component_hover_bg_colour']
        self.display = True
        self.display_children = True

        self.click_event = click_event
        self.hover_event = hover_event
        self.click_disabled = False

    def _step(self,mousestate):

        for child in self.child_components:
            child._step(mousestate)

        if pygame.MOUSEBUTTONDOWN in mousestate:
            # left click 
            if 1 in mousestate[pygame.MOUSEBUTTONDOWN]:
                if self.in_bounds(*mousestate[pygame.MOUSEBUTTONDOWN][1]) and self.display:
                    self.event_click()

    def _draw(self,screen,rm):

        if self.display:
            # draw bg colour
            pygame.draw.rect(screen,self.bg_colour,(self.x,self.y,self.w,self.h),0)

        if self.display_children:
            for child in self.child_components:
                child._draw(screen,rm)

    def add_child_component(self,component):
        self.child_components.append(component)
        return component

    def clear_children(self):
        self.child_components = []

    def in_bounds(self,x,y):
        return (x >= self.x and x <= (self.x+self.w)) and (y >= self.y and y <= (self.y+self.h))

    # events
    def event_hover(self):
        self.hover_event()

    def event_click(self):
        if not self.click_disabled:
            self.click_event()
