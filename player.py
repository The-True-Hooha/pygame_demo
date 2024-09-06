from pygame.locals import *
import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.rect.move_ip(0, -5)
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400 :
            if keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
            
    def draw_player(self, surface):
        surface.blit(self.image, self.rect)