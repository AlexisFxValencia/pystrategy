import pygame

class MapObject:
    def __init__(self, myposition):
        self.position = myposition
        self.radius = 20
        
        
        self.selected = False
        self.unselected_color = "white"
        self.selected_color = "red"
        self.active = True
        self.z = 0

    def check_selection(self, keys):
        if keys[pygame.K_t]:
            self.selected = True        
        if keys[pygame.K_y]:
            self.selected = False

    def check_selection_mouse(self, mouse_vec):        
        distance = mouse_vec - self.position        
        if distance.length_squared() <= (self.radius**2):             
            self.selected = True
        else :
            self.selected = False
   
    
    
    
    


if __name__=="__main__":
    pass