from pygame.locals import *
import pygame
import random

score = 0

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 400 - 40), 0)
        print('do something')
    
    
    def move(self):
        global score
        self.rect.move_ip(0, 5)
        if(self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 400 - 40), 0)
    
    def draw_enemy(self, surface):
        surface.blit(self.image, self.rect)