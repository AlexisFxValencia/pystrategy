
import pygame
from gameObjects.townCenter import TownCenter
from gameObjects.goldMine import GoldMine
from gameObjects.peon import Peon

class GameObjects:
    def __init__(self, screen):
        self.selected_object = None
        self.selected_z = -1
        
        #Creating game objects
        town_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.town = TownCenter(town_position)
        mine_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        mine_position.x+= 400
        mine_position.y+= 200
        self.mine = GoldMine(mine_position)
        self.places = [self.town, self.mine]

        peon_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        mypeon = Peon(peon_position)
        self.peons = [mypeon]
        
        
    
    def draw(self, screen):
        self.draw_list(screen, self.places)
        self.draw_list(screen, self.peons)
        self.draw_gold(screen, self.town.gold)
    
    def draw_list(self, screen, mylist):
        for object in mylist:
            pygame.draw.circle(screen, object.unselected_color, object.position, object.radius)
            if object.selected:
                pygame.draw.circle(screen, object.selected_color, object.position, object.radius, 5)


    def draw_gold(self, screen, gold):
        font = pygame.font.SysFont("Arial", 36)
        txtsurf = font.render("Gold = " + str(gold), True, 'white')
        screen.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))

    def plays(self, dt):
        keys = pygame.key.get_pressed()
        self.play_peons(keys, dt)
        self.play_towns(keys, dt)
    
    def play_peons(self, keys, dt):
        for pe in self.peons:
            if pe.selected:
                pe.update_position(keys, dt)
                pe.mines(keys, self.mine)
                pe.brings_back(keys, self.town)
            
            pe.moves_toward_B(dt)
    
    def play_towns(self, keys, dt):
        if self.town.selected:
            if self.town.create_peon(keys):
                peon_position_local =  pygame.Vector2(self.town.position.x, self.town.position.y) 
                peon_position_local.x += self.town.radius
                pe = Peon(peon_position_local)
                self.peons.append(pe)
    
    def reactivate_peons(self):
        for peon in self.peons:
            peon.active = True
    
    def reactivate_places(self):
        for place in self.places:
            place.active = True

    def update_selected_object(self, mouse_vec):
        local_selected = None
        for p in self.peons:
            p.selected = False
            p.check_selection_mouse(mouse_vec)                    
            if p.selected:
                self.selected_z = p.z
                local_selected = p
        for pl in self.places:
            pl.selected = False
            if pl.z > self.selected_z:
                pl.check_selection_mouse(mouse_vec)   
                if pl.selected:
                    self.selected_z = pl.z
                    local_selected = pl
                    
        self.selected_object = local_selected
        self.selected_z = -1 
    
    def update_automated_movement(mouse_vec):
        if self.selected_object != None :
            self.selected_object.pointA = self.selected_object.position
            self.selected_object.pointB = mouse_vec
            self.selected_object.direction = self.selected_object.pointB - self.selected_object.pointA
            self.selected_object.direction = self.selected_object.direction.normalize()
            
    def write_data(self):    
        mypeon = self.peons[0]
        data = {1 : {"type" : "peon", "id" : 1, "x" : mypeon.position.x, "y" : mypeon.position.y}}
        return data