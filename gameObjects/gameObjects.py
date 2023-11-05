
import pygame
from gameObjects.townCenter import TownCenter
from gameObjects.goldMine import GoldMine
from gameObjects.peon import Peon

class GameObjects:
    def __init__(self, screen):
        self.map_center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.map_width = screen.get_width()
        self.map_height = screen.get_height()
        
        self.selected_object = None
        self.selected_z = -1
        
        #Creating game objects
        self.peons = []
        self.create_first_peons(1)
        
        self.buildings = []
        self.create_first_buildings()
        
        self.map_objects = []
        self.create_map()

        
        
    def create_first_peons(self, n):
        for i in range(n):
            peon_position = pygame.Vector2(self.map_center.x, self.map_center.y)
            peon_position.x += 50*i
            peon = Peon(peon_position)
            peon.z += i            
            self.peons.append(peon)
    
    def create_first_buildings(self):
        town_position = pygame.Vector2(self.map_center.x, self.map_center.y)
        town = TownCenter(town_position)
        self.buildings.append(town)
    
    def create_map(self):
        mine_position = pygame.Vector2(self.map_center.x, self.map_center.y)
        mine_position.x+= 400
        mine_position.y+= 200
        mine = GoldMine(mine_position)
        self.map_objects.append(mine)

    def draws(self, screen):
        self.draws_list(screen, self.map_objects)
        self.draws_list(screen, self.buildings)
        self.draws_list(screen, self.peons)
        self.draws_gold(screen, self.buildings[0].gold)
    
    def draws_list(self, screen, mylist):
        for object in mylist:
            pygame.draw.circle(screen, object.unselected_color, object.position, object.radius)
            if object.selected:
                pygame.draw.circle(screen, object.selected_color, object.position, object.radius, 5)


    def draws_gold(self, screen, gold):
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
                pe.mines(keys, self.map_objects[0])
                pe.brings_back(keys, self.buildings[0])
            
            pe.moves_toward_B(dt)
    
    def play_towns(self, keys, dt):
        if isinstance(self.selected_object, TownCenter):
            town = self.selected_object
            if town.selected:
                if town.create_peon(keys):
                    peon_position_local =  pygame.Vector2(town.position.x, town.position.y) 
                    peon_position_local.x += town.radius
                    pe = Peon(peon_position_local)
                    self.peons.append(pe)
    
    def reactivate_peons(self):
        for peon in self.peons:
            peon.active = True
    
    def reactivate_buildings(self):
        for building in self.buildings:
            building.active = True

    def update_selected_object(self, mouse_vec):
        local_selected = None
        for p in self.peons:
            p.selected = False
            p.check_selection_mouse(mouse_vec)                    
            if p.selected:
                self.selected_z = p.z
                local_selected = p
        for pl in self.buildings:
            pl.selected = False
            if pl.z > self.selected_z:
                pl.check_selection_mouse(mouse_vec)   
                if pl.selected:
                    self.selected_z = pl.z
                    local_selected = pl
                    
        self.selected_object = local_selected
        self.selected_z = -1 
    
    def update_automated_movement(self, mouse_vec):
        if self.selected_object != None :
            self.selected_object.pointA = self.selected_object.position
            self.selected_object.pointB = mouse_vec
            self.selected_object.direction = self.selected_object.pointB - self.selected_object.pointA
            self.selected_object.direction = self.selected_object.direction.normalize()
            
    def write_data(self):    
        #first_peon = self.peons[0]
        data = {}
        for i, pe in enumerate(self.peons):
            temp = {i : {"type" : "peon", "id" : 1, "x" : pe.position.x, "y" : pe.position.y}}
            data.update(temp)
        return data
    
    def draws_other_players(self, screen, data):
        if data != None and len(data) > 0 :
            print("data not empty.")
            for key in data:
                print(key)
                if data[key]["type"] == "peon":
                    color = "red"
                    position = pygame.Vector2(data[key]["x"], data[key]["y"]) 
                    radius = 20
                    pygame.draw.circle(screen, color, position, radius)
                