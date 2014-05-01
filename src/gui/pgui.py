from layouts.boardlayout import BoardLayout

class PGui():

    # components - buttons, text, effects (relatively positioned)
    # templates - collection of components (event handling?) (absolute positioned)
    # layout - collection of templates (for state)

    # to prevent cascading click/hover events... go in this order component->template->layout (break if you find one)
    # this will prevent click event from happening on a template that a component is over top of
    # what about components within components??? maybe they need a z-index

    # TODO template can be a layout... dont need so many levels... components can have multiple childs... hierachy unneccesary

    def __init__(self,game):
        self.g = game
        self._setup_layout(BoardLayout())

    def _setup_layout(self,layout):
        self.cur_layout = layout
        self.cur_layout._setup(self.g)

    def _step(self):
        self._input()
        #TODO should be called mouseevents throughout layout/template/component
        self.cur_layout._step(self.g.im.mouseevents)

    def _draw(self):
        self.cur_layout._draw(self.g.screen)

    def _input(self):
        pass
