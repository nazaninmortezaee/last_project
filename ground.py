import pygame

folder_addres = "./assets/"

class GND:
    img = pygame.image.load(folder_addres + "ground.png")
    def __init__(self, speed, y):
        self.speed = speed
        self.locs = [[0, y] , [2000, y]]

    def update(self, surface):
        #move
        self.locs[0][0] -= self.speed
        self.locs[1][0] -= self.speed
        if self.locs[0][0] == -2000:
            self.locs [0][0]= 2000
        if self.locs[1][0] == -2000:
            self.locs[1][0] = 2000

        #show
        surface.blit(self.img, self.locs[0]) 
        surface.blit(self.img, self.locs[1])


