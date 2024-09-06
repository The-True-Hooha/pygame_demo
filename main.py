from pygame.locals import *
import pygame
import random, time, sys
from enemy import Enemy
from player import Player



pygame.init()

player1 = Player()
npc = Enemy()


game_screen = pygame.display.set_mode((400, 600))
fps = pygame.time.Clock()

#the colors``
SEA_BLUE = (46, 166, 203, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

game_speed = 5
game_score = 0

font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render('GAME OVER', True, BLACK)

background = pygame.image.load('assets/images/street.png')



title = pygame.display.set_caption('some game')

group_npc = pygame.sprite.Group()
group_npc.add(npc)
char = pygame.sprite.Group()
char.add(player1)
char.add(npc)

up_speed = pygame.USEREVENT + 1
pygame.time.set_timer(up_speed, 1000)


while True:
    for i in pygame.event.get():
        if i.type == up_speed:
            game_speed += 10
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
    # player1.update_position()
    # npc.move_enemy()
    game_screen.blit(background, (0, 0))
    scores = font_small.render(str(game_score), True, BLACK)
    game_screen.blit(scores, (10, 10))
    
    
    for i in char:
        game_screen.blit(i.image, i.rect)
        i.move()
        
        # python -m pip
    
    if pygame.sprite.spritecollideany(player1, group_npc):
        game_screen.fill(RED)
        pygame.display.update()
        for e in char:
            e.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    # player1.draw_player(game_screen)
    # npc.draw_enemy(game_screen)
    
    pygame.display.update()
    fps.tick(60)
    
    