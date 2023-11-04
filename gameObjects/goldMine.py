import pygame
from gameObjects.place import Place

class GoldMine(Place):
    def __init__(self, myposition):
        super().__init__(myposition)
        self.radius = 80
        self.unselected_color = "gold"
        self.selected_color = "red"   
        
        self.gold = 20000
        
    
    
    
    


if __name__=="__main__":
    pass