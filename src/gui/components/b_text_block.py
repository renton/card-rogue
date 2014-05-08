from abstractcomponent import AbstractComponent

class BTextBlock(AbstractComponent):

    # value is a lambda
    def __init__(
                    self,
                    x,
                    y,
                    value,
                    bg_colour=(23,32,43),
                    w=0,
                    h=0,
                    display_text=True,
                    click_event=lambda:True,
                    display=False,
                    hover_event=lambda:True,
                ):
        AbstractComponent.__init__(
                                    self,
                                    x,
                                    y,
                                    w,
                                    h,
                                    click_event,
                                    hover_event,
                                )

        self.bg_colour = bg_colour
        self.value = value
        self.display_text = display_text
        self.display = display

    def _draw(self,screen,rm):
        AbstractComponent._draw(self,screen,rm)
        if self.display_text:
            text = rm.font.render(str(self.value()),1,(255,255,255))
            screen.blit(text,(self.x,self.y))

    def show(self):
        self.display = True
        self.display_text = True

    def hide(self):
        self.display = False
        self.display_text = False
