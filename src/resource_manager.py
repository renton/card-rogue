from settings import *
import pygame

class ResourceManager():

    def __init__(self):
        self.fonts = {}
        self._init_fonts()

    def _init_fonts(self):
        for font in SETTINGS['preload_fonts']:
            self.load_font(font)

    def load_font(self,font_string):
        self.fonts[font_string] = pygame.font.SysFont(font_string,16)

    def get_font(self,font_string):
        if font_string in self.fonts:
            return self.fonts[font_string]
        else:
            return None

    @property
    def font(self):
        return self.fonts[SETTINGS['preload_fonts'][0]]
