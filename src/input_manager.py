import pygame

class InputManager():

    def __init__(self):

        # init keyboard
        self.keystate = {}
        self.keyevents = {}

        # init mouse
        self.mousestate = {}
        self.mouse_x,self.mouse_y = (0,0)

    # EVENTS
    def reset_events(self):
        self.keyevents = {}

    # KEY EVENTS
    def set_key_event(self,event,key):
        if event not in self.keyevents:
            self.keyevents[event] = {}
        self.keyevents[event][key] = 1

    def is_key_event(self,event,key):
        return (event in self.keyevents and key in self.keyevents[event])

    def _fetch_inputs(self):
        self.keystate = pygame.key.get_pressed()
        self.mousestate = pygame.mouse.get_pressed()
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()

    def update(self):
        self._fetch_inputs()
