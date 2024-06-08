#print("main.py is being run")

import pygame
import sys
from constants import *
from nazi import Nazi
from ground import GND
from day import DayOrNight

class Game:
    fps = 60
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((WINDOW_SIZE))
        pygame.display.set_caption(GAME_TITLE)
        self.font = pygame.font.Font(None, 22)
        self.high_score = self.load_high_score()
        self.score = 0
        self.day = DayOrNight(self.fps, 7)
        self.ground = GND(5, WINDOW_SIZE[1]-150)
        self.player1 = Nazi(Nazi_location ,  self.fps)
        self.clock = pygame.time.Clock()
        self.run()


    def load_high_score(self):
        with open("save.txt", "r") as file:
            high_score = file.read()
            return high_score

    def show_score(self, color):
        score = str(self.score)
        _score = self.font.render((6 - len(score))* "0" + score , True, color)
        _hscore =  self.font.render("Hsc " + self.high_score, True, color)
        self.game_display.blit(_score, (890, 40))
        self.game_display.blit(_hscore, (770, 40))
    
    def best_score(self):
        if int(self.high_score) < self.score:
            with open("save.txt", "w") as file:
                _str = (6 - len(str(self.score)))* "0" + str(self.score)
                file.write(_str)



    def run(self):
        while True:
            cur_color = self.day.update(self.game_display)
            self.show_score(cur_color)  # اضافه کردن رنگ سفید به عنوان پارامتر
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player1.jump()
            self.ground.update(self.game_display)
            self.player1.update(self.game_display)
            pygame.display.update()
            self.score += 1
            self.clock.tick(self.fps)


new_game = Game()
