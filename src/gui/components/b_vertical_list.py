from abstractcomponent import AbstractComponent

class BVerticalList(AbstractComponent):

    def __init__(self,x,y,item_keys,item_values):
        AbstractComponent.__init__(
                                    self,
                                    x,
                                    y,
                                    0,
                                    0
                                )
        self._build_list(item_keys,item_values)

    def _build_list():
        pass
