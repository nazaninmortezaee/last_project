import pygame
import sys
from constants import *
from nazi import Nazi
from ground import GND
from day import DayOrNight
from obstacle import obstacle, obstacles

class Game:
    fps = 60 
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(GAME_TITLE)
        self.font = pygame.font.Font(None, 22)
        self.high_score = self.load_high_score()
        self.score = 0
        self.day = DayOrNight(self.fps, 7)
        self.ground = GND(5, WINDOW_SIZE[1] - 150)
        self.obss = obstacles(y=440, min_gap=450, speed=5)
        self.player1 = Nazi(Nazi_location, self.fps)
        self.clock = pygame.time.Clock()

        # Load sounds
        self.jump_sound = pygame.mixer.Sound("./assets/jump.wav")
        self.game_over_sound = pygame.mixer.Sound("./assets/game_over.wav")
        self.background_music = "./assets/background.wav"  # Use WAV for background music 
        
        # Play background music
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)  # Play the background music in a loop

        self.run()

    def load_high_score(self):
        try:
            with open("save.txt", "r") as file:
                high_score = file.read()
                return high_score
        except FileNotFoundError:
            return "000000"

    def show_score(self, color):
        score = str(self.score)
        _score = self.font.render((6 - len(score)) * "0" + score, True, color)
        _hscore = self.font.render("Hsc " + self.high_score, True, color)
        self.game_display.blit(_score, (890, 40))
        self.game_display.blit(_hscore, (770, 40))

    def best_score(self):
        if int(self.high_score) < self.score:
            with open("save.txt", "w") as file:
                _str = (6 - len(str(self.score))) * "0" + str(self.score)
                file.write(_str)
            self.high_score = _str

    def game_over(self, color):
        # show "Game Over", "Your Score" , "High Score" and "Replay"
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        self.game_display.blit(text, (WINDOW_SIZE[0] // 2 - text.get_width() // 2, WINDOW_SIZE[1] // 3))

        score_text = self.font.render(f"Your Score: {self.score:06}", True, color)
        self.game_display.blit(score_text, (WINDOW_SIZE[0] // 2 - score_text.get_width() // 2, WINDOW_SIZE[1] // 2))

        high_score_text = self.font.render(f"High Score: {self.high_score}", True, color)
        self.game_display.blit(high_score_text, (WINDOW_SIZE[0] // 2 - high_score_text.get_width() // 2, WINDOW_SIZE[1] // 2 + 40))

        replay_text = self.font.render("Press R to Replay", True, color)
        self.game_display.blit(replay_text, (WINDOW_SIZE[0] // 2 - replay_text.get_width() // 2, WINDOW_SIZE[1] // 2 + 80))

        pygame.display.update()

        # Play game over sound
        self.game_over_sound.play()

        # Stop background music
        pygame.mixer.music.stop()

        # wait for player
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # click "R" for reset game
                        self.reset_game()
                        return

    def reset_game(self):
        # reset game
        self.score = 0
        self.player1 = Nazi(Nazi_location, self.fps)
        self.obss = obstacles(y=440, min_gap=450, speed=5)

        # Restart background music
        pygame.mixer.music.play(-1)

        self.run()

    def run(self):
        state = True
        while True:
            cur_color = self.day.update(self.game_display, state)
            self.show_score(cur_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player1.jump()
                        self.jump_sound.play()  # Play jump sound

            self.ground.update(self.game_display, state)
            self.obss.update(self.game_display, state)
            state = self.player1.update(self.game_display, self.obss, state)
            self.obss.check()
            if state:
                self.score += 1
            else:
                self.best_score()
                game_over_color = (0, 0, 0) if self.day.is_day else (255, 255, 255)
                self.game_over(game_over_color)

            pygame.display.update()
            self.clock.tick(self.fps)

new_game = Game()
