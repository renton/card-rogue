from layouts.boardlayout import BoardLayout

class PGui():

    # components - buttons, text, effects (relatively positioned)
    # templates - collection of components (event handling?) (absolute positioned)
    # layout - collection of templates (for state)

    def __init__(self,game):
        self.g = game
        self.cur_layout = BoardLayout()

    def _step(self):
        self.cur_layout._step()

    def _draw(self):
        self.cur_layout._draw(self.g.screen)

    def _input(self):
        self.cur_layout._input()
