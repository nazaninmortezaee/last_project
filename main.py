import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.pygame_display = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Dino Game")

        self.run()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    sys.exit

            pygame.display.update() 

new_game = Game()
            


    



            

