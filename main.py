import pgzrun
import pygame
from tasks import tasks

WIDTH = 800
HEIGHT = 600
TITLE = "Maxie"

maxie = Actor('maxie', anchor=('left', 'top'))
maxie.pos = (100, 100)
maxie._surf = pygame.transform.scale(maxie._surf, (200, 200))

def draw():
    bg_color = (50, 150, 50) if tasks[1]["checked"] else (100, 100, 100)
    screen.fill(bg_color)  
    
    maxie.opacity = 100 if tasks[2]["checked"] else 255
    maxie.draw()

    for task in tasks:
        screen.draw.rect(task["box"], "lightblue")

        if task["checked"]:
            screen.draw.filled_rect(
                task["box"],
                "lightgreen"
            )
        
        screen.draw.text(
            task["label"], 
            (480, task["box"].y - 10),
            fontname="margarine_regular",
            fontsize=30,
        )

        screen.draw.text(
            "Maxie", 
            (maxie.x + 10, maxie.y - 60), 
            fontname="margarine_regular",
            fontsize=46,
            color="lightblue",
            shadow=(1, 1),
            scolor="darkblue",
        )
    
def on_mouse_down(pos):
    for task in tasks:
        if task["box"].collidepoint(pos):
            task["checked"] = not task["checked"]
        

    
    
pgzrun.go()
