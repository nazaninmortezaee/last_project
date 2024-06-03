print("main.py is being run")

import pygame
import sys
from constants import *
from nazi import Nazi


class Game:
    fps = 60
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Nazi Game")
        self.font = pygame.font.Font(None, 22)
        self.high_score = self.load_high_score()
        self.score = 0
        self.player1 = Nazi((100, 410), self.fps)
        self.clock = pygame.time.Clock()
        self.run()


    def load_high_score(self):
        with open("save.txt", "r") as file:
            high_score = file.read()
            return high_score

    def show_score(self):
        score = str(self.score)
        _score = self.font.render((6 - len(score))* "0" + score , True, WHITE)
        _hscore =  self.font.render("Hsc " + self.high_score, True, WHITE)
        self.game_display.blit(_score, (890, 40))
        self.game_display.blit(_hscore, (770, 40))
    
    def best_score(self):
        if int(self.high_score) < self.score:
            with open("save.txt", "w") as file:
                _str = (6 - len(str(self.score)))* "0" + str(self.score)
                file.write(_str)



    def run(self):
        rect1= pygame.Rect(500, 420, 30, 30)
        ground = pygame.image.load("./assets/desert.png")
        while True:
            self.game_display.fill((0, 0, 0))
            self.show_score()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player1.jump()
            
            rect1.x -= 3
            pygame.draw.rect(self.game_display, (255, 255, 255), rect1)
            if rect1.colliderect(self.player1.rect):
                print("Collition!")
                self.best_score()
                pygame.quit()
                sys.exit()
                                 
           
            self.game_display.blit(ground, (0,450))
            self.player1.update(self.game_display)
            pygame.display.update()
            self.score += 1
            self.clock.tick(self.fps)

new_game = Game()
