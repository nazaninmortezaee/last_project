print("main.py is being run")

import pygame
import sys
from nazi import Nazi

class Game:
    fps = 60
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Nazi Game")

        self.player1 = Nazi((500, 300), self.fps)
        self.clock = pygame.time.Clock()

        self.run()

    def run(self):
        while True:
            self.game_display.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player1.update(self.game_display)
            pygame.display.update()
            self.clock.tick(self.fps)

new_game = Game()
