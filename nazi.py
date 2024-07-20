print("nazi.py is being imported")

import pygame

folder_addres = "./assets/"

class Nazi:
    i_walk1 = pygame.image.load(folder_addres + "walk1.png")
    i_walk2 = pygame.image.load(folder_addres + "walk2.png")
    i_jump  = pygame.image.load(folder_addres + "jump.png")
    rects_vals = [[13, 17, 42, 31],
            [23, 47, 21, 37],
            [43, 65, 4, 11],
            [46, 70, 4, 11],
            [49, 80, 7, 7],
            [22, 84, 9, 9],
            [19, 92, 8, 7],
            [16, 98, 8, 8],
            [12, 105, 9, 14],
            [36, 84, 15, 10],
            [39, 93, 7, 8],
            [34, 100, 9, 5],
            [30, 104, 10, 12]
    ]

    def __init__(self, location, fps):
        self.location = location
        self.x_loc, self.y_loc = location
        self.Y_LOC = self.y_loc
        self.fps = fps
        self.w_img = True
        self.w_slicer = 8
        self.w_counter = 0
        self.state = True
        self.j_threshold = self.y_loc - 200
        self.double_jump_threshold = self.y_loc - 300  # Double jump threshold
        self.YD = 5  # ydirection hamishegi
        self.yd = self.YD
        self.rect = self.i_walk1.get_rect(topleft=self.location)
        self.rects = self.create_rects()
        self.jump_count = 0  # To keep track of jump counts

    def create_rects(self):
        rects = []
        for rect in self.rects_vals:
            rects.append(pygame.Rect(rect[0] + self.x_loc, rect[1] + self.y_loc, rect[2], rect[3]))
        return rects

    def update_rects(self):
        for i in range(len(self.rects)):
            self.rects[i].y -= self.yd

    def update(self, surface, objs, state):
        # pygame.draw.rect(surface, "red", self.rect)

        if state is None:
            if self.state:
                surface.blit(self.i_walk1, self.location)
            else:
                surface.blit(self.i_jump, (self.x_loc, self.y_loc))
            return None

        for i in range(len(objs.obs_list)):
            for obj_rect in objs.obs_list[i].rects:
                for nazi_rect in self.rects:
                    if nazi_rect.colliderect(obj_rect):
                        return None

        # for rect in self.rects:
        #     pygame.draw.rect(surface, "pink", rect)
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
            if self.yd > 0:  # going up
                if self.jump_count == 1 and self.y_loc < self.j_threshold:
                    self.yd *= -1
                elif self.jump_count == 2 and self.y_loc < self.double_jump_threshold:
                    self.yd *= -1
            else:  # going down
                if self.y_loc > self.Y_LOC:
                    self.state = True
                    self.yd = self.YD
                    self.jump_count = 0  # Reset jump count when landing
            self.y_loc -= self.yd
            surface.blit(self.i_jump, (self.x_loc, self.y_loc))
            self.rect.topleft = (self.x_loc, self.y_loc)
            self.update_rects()
        return True

    def jump(self):
        if self.state or self.jump_count < 2:  # Allow double jump
            self.state = False
            self.jump_count += 1
            if self.jump_count == 2:
                self.yd = self.YD  # Reset y direction for double jump
