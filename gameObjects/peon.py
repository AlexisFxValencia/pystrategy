import pygame

from gameObjects.place import Place
from gameObjects.constants import *

class Peon(Place):
    def __init__(self, position):
        super().__init__(position)
        self.radius = PEON_RADIUS
        self.unselected_color = PEON_unselected_color
        self.selected_color = PEON_selected_color
        
        self.speed = PEON_SPEED
        self.pointA = pygame.Vector2(0, 0)
        self.pointB = pygame.Vector2(0, 0)
        self.direction = pygame.Vector2(0, 0)
        self.gold = 0
        self.z = PEON_Z
    
    def set_pointA(self, pointA1):
        self.pointA = pointA1
    
            
    def update_position(self, keys, dt):
        if keys[pygame.K_z]:
            self.position.y -= PEON_KEYBOARD_SPEED * dt
        if keys[pygame.K_s]:
            self.position.y += PEON_KEYBOARD_SPEED * dt
        if keys[pygame.K_q]:
            self.position.x -= PEON_KEYBOARD_SPEED * dt
        if keys[pygame.K_d]:
            self.position.x += PEON_KEYBOARD_SPEED * dt
    
    def mines(self, keys, mine):
        if self.active and self.gold < PEON_GOLD_CAPACITY:
            if keys[pygame.K_m]:
                distance = self.position - mine.position
                criterion = float((self.radius + mine.radius)**2)
                
                if distance.length_squared() <= criterion:
                    self.gold = PEON_GOLD_CAPACITY
                    self.active = False

    def brings_back(self, keys, town):
        if self.active and self.gold > 0:
            if keys[pygame.K_m]:
                distance = self.position - town.position
                criterion = float((self.radius + town.radius)**2)
                
                if distance.length_squared() <= criterion:
                    town.gold += self.gold
                    self.gold = 0
                    self.active = False

    def moves_toward_B(self, dt):
        if (self.pointB.x != 0) and (self.pointB.y != 0) :
            distance = self.pointB - self.pointA
            if distance.length_squared() > (self.radius**2)/10:
                self.position += self.direction*self.speed*dt
            else :
                self.pointB.x = 0
                self.pointB.y = 0
                
            



if __name__=="__main__":
    pass