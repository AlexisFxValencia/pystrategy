
import pygame
from gameObjects.townCenter import TownCenter
from gameObjects.goldMine import GoldMine
from gameObjects.peon import Peon

class GameObjects:
    def __init__(self, screen):
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
        
        self.selected_object = None
        self.selected_z = -1
        