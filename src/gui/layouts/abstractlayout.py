from ..gui_settings import *

class AbstractLayout():

    def __init__(self):
        self.bg_colour = G_SETTINGS['default_bg_colour']

        self.templates = []

    def _step(self):
        for template in self.templates:
            template._step()

    def _draw(self,screen):
        screen.fill(self.bg_colour)
        for template in self.templates:
            template._draw(screen)

    def _input(self):
        pass

    def add_template(self,template):
        self.templates.append(template)
