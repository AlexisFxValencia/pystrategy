import pygame
from place import Place

class GoldMine(Place):
    def __init__(self, myposition):
        super().__init__(myposition)
        self.radius = 80
        self.color = "yellow"        
        self.gold = 20000
        
    
    
    
    


if __name__=="__main__":
    pass