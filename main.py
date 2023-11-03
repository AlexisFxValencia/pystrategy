# Example file showing a circle moving on screen
import pygame

from townCenter import TownCenter
from goldMine import GoldMine
from peon import Peon

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

time_elapsed_since_last_action = 0



town_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
town = TownCenter(town_position)

mine_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
mine_position.x+= 400
mine_position.y+= 200
mine = GoldMine(mine_position)

places = [town, mine]

peon_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
mypeon = Peon(peon_position)

peons = [mypeon]

def draw_list(mylist):
    for object in mylist:
        pygame.draw.circle(screen, object.color, object.position, object.radius)

def activate_list(mylist):
    for object in mylist:
        object.active = True

def draw_gold(gold):
    font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render("Gold = " + str(gold), True, 'white')
    screen.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    draw_list(places)
    draw_list(peons)
    draw_gold(town.gold)
    
    

    keys = pygame.key.get_pressed()
    mypeon.check_selection(keys)
    if mypeon.selected:
        mypeon.update_position(keys, dt)
        mypeon.mines(keys, mine)
        mypeon.brings_back(keys, town)
    
    
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    
    
    time_elapsed_since_last_action += dt
    
    # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
    if time_elapsed_since_last_action > 1:
        #print(time_elapsed_since_last_action)
        activate_list(peons)
        time_elapsed_since_last_action = 0 # reset it to 0 so you can count again


pygame.quit()