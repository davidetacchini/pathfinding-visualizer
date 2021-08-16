from consts import *


class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.width = 120
        self.height = 40
        self.bg_color = Color.WHITE
        self.text_color = Color.DARK_GREY
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
    
    def __call__(self, window, font):
        pg.draw.rect(window, self.bg_color, self.rect)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect()
        text_rect.center = (self.x + (self.width / 2), self.y + (self.height / 2))
        window.blit(text, text_rect)

    def is_clicked(self, pos, event):
        return self.rect.collidepoint(pos) and event.button == 1 # left click
