import pygame
from gameObjects.gameObjects import GameObjects
from client import *
from random import randint
import json

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
time_elapsed_since_last_action = 0


#creating a room or joining the first available room
client_port = randint(500, 2000)
server_port = 1234
server_ip = "127.0.0.1"
myclient = Client(server_ip, server_port, server_port, client_port)

print("Client 1 : %s" % myclient.identifier)
rooms = myclient.get_rooms()
print(rooms)
if len(rooms) == 0:
    myclient.create_room("Test room")
    print("myclient creates room  %s" % myclient.room_id)
    rooms = myclient.get_rooms()
else:
    selected_room = rooms[0]['id']
    myclient.join_room(selected_room)
    print("myclient joins room  %s" % myclient.room_id)


go = GameObjects(screen)


def share_data(myclient, mypeon):
    data = {"mypeon.position.x":mypeon.position.x, "mypeon.position.y":mypeon.position.y}
    json_data = json.dumps(data)
    myclient.send(json_data)
    messages = myclient.get_messages()
    if len(messages) != 0:
        for message in messages:
            message = json.loads(message)
            sender, value = message.popitem()
            print(sender)
            print(myclient.identifier)
            data = json.loads(value)
            print(data["mypeon.position.x"])


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
            myclient.leave_room()
        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            mouse_vec =  pygame.Vector2(mouse_pos)
            
            if event.button == 1: #left click
                local_selected = None
                for p in go.peons:
                    p.selected = False
                    p.check_selection_mouse(mouse_vec)                    
                    if p.selected:
                        go.selected_z = p.z
                        local_selected = p
                for pl in go.places:
                    pl.selected = False
                    if pl.z > go.selected_z:
                        pl.check_selection_mouse(mouse_vec)   
                        if pl.selected:
                            go.selected_z = pl.z
                            local_selected = pl
                            
                go.selected_object = local_selected
                go.selected_z = -1 
                
            elif event.button == 3: #right click
                if go.selected_object != None :
                    go.selected_object.pointA = go.selected_object.position
                    go.selected_object.pointB = mouse_vec
                    go.selected_object.direction = go.selected_object.pointB - go.selected_object.pointA
                    go.selected_object.direction = go.selected_object.direction.normalize()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")    
    go.draw(screen)
    go.plays(dt)
    
     
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000    
    time_elapsed_since_last_action += dt
    
    # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
    if time_elapsed_since_last_action > 1:
        go.reactivate_peons()
        go.reactivate_places()
        time_elapsed_since_last_action = 0 # reset it to 0 so you can count again
        share_data(myclient, go.peons[0])




pygame.quit()