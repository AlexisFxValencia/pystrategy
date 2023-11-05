import pygame
from gameObjects.place import Place
from gameObjects.constants import *

class GoldMine(Place):
    def __init__(self, myposition):
        super().__init__(myposition)
        self.radius = MINE_RADIUS
        self.unselected_color = "gold"
        self.selected_color = "red"   
        
        self.gold = MINE_CAPACITY
        
    
    
    
    


if __name__=="__main__":
    pass