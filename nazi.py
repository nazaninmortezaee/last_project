print("nazi.py is being imported")

import pygame

folder_addres = "./assets/"

class Nazi:
    i_walk1 = pygame.image.load(folder_addres + "walk1.png")
    i_walk2 = pygame.image.load(folder_addres + "walk2.png")
    i_jump  = pygame.image.load(folder_addres + "jump.png")

    def __init__(self, location, fps):
        self.location = location
        self.x_loc, self.y_loc = location
        self.fps = fps
        self.w_img = True
        self.w_slicer = 8
        self.w_counter = 0

    def update(self, surface):
        if self.w_counter < self.fps:
            if self.w_counter % self.w_slicer == 0:
                self.w_img = not self.w_img
            self.w_counter += 1
        else:
            self.w_counter = 0
        if self.w_img:
            surface.blit(self.i_walk1, self.location)
        else:
            surface.blit(self.i_walk2, self.location)
        
