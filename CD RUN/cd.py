import pygame
class Cd: 
    def __init__(self):
        self.sprite = pygame.image.load('static/images/cd.png')
        self.position = pygame.Vector2()
        self.position.xy