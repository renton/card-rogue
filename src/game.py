import sys,pygame
from pygame.locals import *
from settings import *
from resource_manager import ResourceManager
from input_manager import InputManager

from states import BoardState

class Game():

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.fps = SETTINGS['default_fps']

        # fullscreen on/off
        if SETTINGS['fullscreen_mode']:
            self.screen = pygame.display.set_mode((
                                                    SETTINGS['window_x_size'],
                                                    SETTINGS['window_y_size']
                                                    ),
                                                    pygame.FULLSCREEN
                                                )
        else:
            self.screen = pygame.display.set_mode((
                                                    SETTINGS['window_x_size'],
                                                    SETTINGS['window_y_size']
                                                ))

        # load resource manager
        self.rm = ResourceManager()

        # load input manager
        self.im = InputManager()

        # state setup
        self.cur_state = BoardState(self.screen,self.rm)

    def _step(self):
        self.cur_state._step()

    def _draw(self):
        self.screen.fill((120,120,150))
        self.cur_state._draw()

    def mainloop(self):
        while(1):

            # reset im key events
            self.im.reset_events()

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.im.set_key_event(event.type,event.key)
                if event.type == pygame.JOYBUTTONDOWN:
                    self.im.set_joy_button_event(event.type,event.button)


            # let state handle input
            self.im.update()
            self.cur_state._input(self.im)

            # draw frame
            self._draw()
            self.clock.tick(self.fps)
            pygame.display.flip()

            # step frame
            self._step()
