import pygame

class DayOrNight:
    def __init__(self, fps, length):
        self.threshold = fps * length
        self.counter = 0
        self.state = True
        self.c = 0
        self.transition_speed = 2
        self.transition = False
        self.is_day = True

        # Load background images
        self.day_image = pygame.image.load("./assets/day_background.png")
        self.night_image = pygame.image.load("./assets/night_background.png")

        # Add variables for background movement
        self.bg_x = 0
        self.bg_speed = 2  # Speed of background movement

    def update(self, surface, state):
        if state:
            _max = 255 - self.transition_speed
            _min = 0 - self.transition_speed
            if self.transition:
                self.c += self.transition_speed
            if self.c >= _max or self.c < _min:
                self.transition_speed *= -1
                self.transition = False
            self._update()
            self.is_day = self.c >= 128  # تعیین وضعیت روز یا شب بر اساس مقدار روشنایی

        # Move the background
        self.bg_x -= self.bg_speed
        if self.bg_x <= -self.day_image.get_width():
            self.bg_x = 0

        # Draw the appropriate background image
        if self.is_day:
            surface.blit(self.day_image, (self.bg_x, 0))
            surface.blit(self.day_image, (self.bg_x + self.day_image.get_width(), 0))
        else:
            surface.blit(self.night_image, (self.bg_x, 0))
            surface.blit(self.night_image, (self.bg_x + self.night_image.get_width(), 0))

        return (0, 0, 0) if self.is_day else (255, 255, 255)

    def _update(self):
        if not self.transition:
            if self.counter >= self.threshold:
                self.transition = True
                self.counter = 0
            else:
                self.counter += 1
