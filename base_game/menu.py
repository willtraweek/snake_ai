import pygame


class Menu:
    score = 0
    high_score = 0

    def __init__(self, menu_width, window_width, window_height, background_color):
        self.font = pygame.font.SysFont("Verdana", 20)
        self.menu_width = menu_width
        self.window_width = window_width
        self.window_height = window_height
        self.background_color = background_color

    def draw(self, display):
        # CLEAR THE MENU
        display.fill(self.background_color, (0, 0, self.window_width, self.window_height))

        scorecard = self.font.render(f"Score: {self.score}", True, pygame.Color("black"))
        display.blit(scorecard, (10, 10))

        scorecard = self.font.render(f"High Score: {self.high_score}", True, pygame.Color("black"))
        display.blit(scorecard, (10, 30))

    @staticmethod
    def reset_score():
        if Menu.score > Menu.high_score:
            Menu.high_score = Menu.score

        Menu.score = 0
