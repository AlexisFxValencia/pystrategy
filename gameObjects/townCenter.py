import pygame
from gameObjects.place import Place
from gameObjects.constants import *

class TownCenter(Place):
    def __init__(self, myposition):
        super().__init__(myposition)
        self.radius = TOWN_RADIUS        
        self.unselected_color = TOWN_unselected_color
        self.selected_color = TOWN_selected_color        
        self.gold = TOWN_initial_gold
        
    def create_peon(self, keys):
        if self.active:
            if keys[pygame.K_m]:
                if self.gold > TOWN_PEON_COST:
                    self.gold -= TOWN_PEON_COST
                    self.active = False
                    return True
        return False
            
    
    
    


if __name__=="__main__":
    pass