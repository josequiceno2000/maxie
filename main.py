import pgzrun
import pygame

WIDTH = 800
HEIGHT = 600
TITLE = "Maxie"

maxie = Actor('maxie', anchor=('left', 'top'))
maxie.pos = (100, 100)
maxie._surf = pygame.transform.scale(maxie._surf, (200, 200))

def draw():
    screen.clear()  # Purple background
    maxie.draw()
    
pgzrun.go()
