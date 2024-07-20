import pygame
from random import randint as rnd

folder_addres = "./assets/"

def load_obj_rects_details(name):
    with open(folder_addres + name[:-3] + "txt") as file:
        content = file.readlines()
        content = [i.strip() for i in content]
        content = [i.split(",") for i in content]
        content = [[int(j) for j in i] for i in content]
    return content

class obstacles:
    def __init__(self, y, min_gap, speed):
        self.obs_list = []
        self.y_loc = 440
        self.min_gap = min_gap
        self.speed = speed
        self.init_obss()

    def init_obss(self):
        self.obs_list.append(obstacle((rnd(700, 1000), self.y_loc), self.speed))
        self.obs_list.append(obstacle((rnd(1450, 1750), self.y_loc), self.speed))
        self.obs_list.append(obstacle((rnd(2200, 2750), self.y_loc), self.speed))

    def remove(self):
        self.obs_list.pop(0)

    def gen_obs(self):
        self.obs_list.append(obstacle((rnd(2000, 2300), self.y_loc), self.speed))

    def check(self):
        if self.obs_list[0].x_loc + self.obs_list[0].width < 0:
            self.remove()
        if self.obs_list[-1].x_loc + self.obs_list[-1].width + self.min_gap < 2000:
            self.gen_obs()

    def update(self, surface, state):
        for obs in self.obs_list:
            obs.update(surface, state)

class obstacle:
    img_list = [
        ["day1.png", load_obj_rects_details("day1.png")],
        ["day2.png", load_obj_rects_details("day2.png")],
        ["day3.png", load_obj_rects_details("day3.png")],
        ["day4.png", load_obj_rects_details("day4.png")],
        ["night1.png", load_obj_rects_details("night1.png")],
        ["night2.png", load_obj_rects_details("night2.png")],
        ["night3.png", load_obj_rects_details("night3.png")],
        ["night4.png", load_obj_rects_details("night4.png")]

    ]

    def __init__(self, location, speed):
        self.location = location
        self.x_loc, self.y_loc = location
        self.speed = speed
        self.type = rnd(0, len(self.img_list) - 1)
        self.img = pygame.image.load(folder_addres + self.img_list[self.type][0])
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        # Adjust y_loc based on the height of the image
        self.y_loc = 530 - self.height  # Ensure y location is the same for all objects

        self.rect = self.img.get_rect(topleft=(self.x_loc, self.y_loc))
        self.rects = self.create_rects()

    def create_rects(self):
        rects = []
        for rect_details in self.img_list[self.type][1:]:
            for each_rect in rect_details:
                rects.append(pygame.Rect(each_rect[0] + self.x_loc, 
                                         each_rect[1] + self.y_loc,
                                         each_rect[2],
                                         each_rect[3]))
        return rects

    def update(self, surface, state):
        if state:
            self.x_loc -= self.speed
            self.rect.x -= self.speed
        surface.blit(self.img, (self.x_loc, self.y_loc))
        if state:
            for i in range(len(self.rects)):
                self.rects[i].x -= self.speed
                # pygame.draw.rect(surface, "red", self.rects[i], 1)
