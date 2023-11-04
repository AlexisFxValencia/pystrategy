import pygame
from gameObjects.place import Place

class TownCenter(Place):
    def __init__(self, myposition):
        super().__init__(myposition)
        self.radius = 120        
        self.unselected_color = "green"
        self.selected_color = "red"        
        self.gold = 133
        
    def create_peon(self, keys):
        if keys[pygame.K_m]:
            if self.gold > 50:
                self.gold -= 50
                return True
        return False
            
    
    
    


if __name__=="__main__":
    pass