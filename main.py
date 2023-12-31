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


#Game Objects
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

selected_object = None
selected_z = -1

def draw_list(mylist):
    for object in mylist:
        pygame.draw.circle(screen, object.unselected_color, object.position, object.radius)
        if object.selected:
            pygame.draw.circle(screen, object.selected_color, object.position, object.radius, 5)

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
        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            mouse_vec =  pygame.Vector2(mouse_pos)
            
            if event.button == 1: #left click
                local_selected = None
                for p in peons:
                    p.selected = False
                    p.check_selection_mouse(mouse_vec)                    
                    if p.selected:
                        selected_z = p.z
                        local_selected = p
                for pl in places:
                    pl.selected = False
                    if pl.z > selected_z:
                        pl.check_selection_mouse(mouse_vec)   
                        if pl.selected:
                            selected_z = pl.z
                            local_selected = pl
                            
                selected_object = local_selected
                selected_z = -1 
                
            elif event.button == 3: #right click
                if selected_object != None :
                    selected_object.pointA = selected_object.position
                    selected_object.pointB = mouse_vec
                    selected_object.direction = selected_object.pointB - selected_object.pointA
                    selected_object.direction = selected_object.direction.normalize()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    draw_list(places)
    draw_list(peons)
    draw_gold(town.gold)
    
    

    keys = pygame.key.get_pressed()
    mypeon.check_selection(keys)
    for pe in peons:
        if pe.selected:
            pe.update_position(keys, dt)
            pe.mines(keys, mine)
            pe.brings_back(keys, town)
        
    for pe in peons:
        pe.moves_toward_B(dt)
    
    if town.selected:
        if town.create_peon(keys):
            peon_position_local =  pygame.Vector2(town.position.x,town.position.y) 
            peon_position_local.x += town.radius
            pe = Peon(peon_position_local)
            peons.append(pe)
    
    

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