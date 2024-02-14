import pygame
class Button:
    def __init__(self):
        self.price = 3
        self.level = 1   
    sprite = pygame.image.load('static/images/button.png')
    typeIndicatorSprite = pygame.image.load('static/images/null_indicator.png')