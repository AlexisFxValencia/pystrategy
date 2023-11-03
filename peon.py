import pygame

class Peon:
    def __init__(self, position):
        self.position = position
        self.speed = 20
        self.selected = False
        self.pointA = pygame.Vector2(0, 0)
        self.pointB = pygame.Vector2(0, 0)
        self.gold = 0
        self.radius = 20
        self.color = "red"
        self.active = True
    
    def set_pointA(self, pointA1):
        self.pointA = pointA1
    
    def check_selection(self, keys):
        if keys[pygame.K_t]:
            self.color = "blue"
            self.selected = True
        
        if keys[pygame.K_y]:
            self.color = "red"
            self.selected = False
    
    def update_position(self, keys, dt):
        if keys[pygame.K_z]:
            self.position.y -= 300 * dt
        if keys[pygame.K_s]:
            self.position.y += 300 * dt
        if keys[pygame.K_q]:
            self.position.x -= 300 * dt
        if keys[pygame.K_d]:
            self.position.x += 300 * dt
    
    def mines(self, keys, mine):
        if self.active:
            if keys[pygame.K_m]:
                distance = self.position - mine.position
                criterion = float((self.radius + mine.radius)**2)
                
                if distance.length_squared() <= criterion:
                    self.gold = 10
                    print(self.gold)
                    self.active = False

    def brings_back(self, keys, town):
        if self.active:
            if keys[pygame.K_m]:
                distance = self.position - town.position
                criterion = float((self.radius + town.radius)**2)
                
                if distance.length_squared() <= criterion:
                    self.gold = 0
                    print(self.gold)  
                    town.gold += 10
                    self.active = False




if __name__=="__main__":
    pass