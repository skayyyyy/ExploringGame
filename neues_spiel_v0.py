# Gameloop läuft, display wird ausgeben und exit ist möglich
#next up: game saves and highscores

# Libraries and Copyright
import pygame
import random
import math

# Screen 
w = 700
h = 500
screen = pygame.display.set_mode((w, h), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption("Placeholder")
print(w,h)

# Display (add colours for text)
FPS = 60
clock = pygame.time.Clock()

#Textausgabe


mode = 0
# 0 intro
# 1 Init
# 2 Game
# Pause
# Menu
# Actions
# Inventory
# Gameover


# Levellayout
level0 = [] # tutorial incl.
level1 = []
level2 = []


# Figures (MC, NPCs, mobs, bosses)

pygame.init()


# Loop nur Berechung
running = True
while running == True:
    clock.tick(FPS)
    keystate = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if  keystate[pygame.K_ESCAPE] == True:
        running = False
    
# Drawing nur Ausgabe

pygame.quit()