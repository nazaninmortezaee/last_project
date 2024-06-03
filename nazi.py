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
        self.Y_LOC = self.y_loc
        self.fps = fps
        self.w_img = True
        self.w_slicer = 8
        self.w_counter = 0
        self.state = True
        self.j_threshold = self.y_loc - 250
        self.YD = 5 #ydirection hamishegi
        self.yd = self.YD
        self.rect = self.i_walk1.get_rect(topleft = self.location)

    def update(self, surface):
        if self.state:
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
        else:
            if self.yd > 0 : #going up
                if self.y_loc < self.j_threshold:
                    self.yd *= -1
            else: #going down
                if self.y_loc > self.Y_LOC:
                    self.state = True
                    self.yd = self.YD
            self.y_loc -= self.yd
            surface.blit(self.i_jump, (self.x_loc, self.y_loc))
            self.rect.topleft = (self.x_loc, self.y_loc)
    def jump(self):
        self.state = False                
        
