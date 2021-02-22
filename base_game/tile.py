import pygame
from enum import Enum


class TileType(Enum):
    BLANK = 0
    FOOD = 1


class Tile:
    def __init__(self, pos: (int, int), size: int, color: (int, int, int) = (0, 0, 0)):
        self.surface = pygame.Surface((size, size))
        self.pos = pos
        self.color = color
        self.rect = self.surface.get_rect(center=pos)
        self.type = TileType.BLANK

    def draw(self, display_surface):
        display_surface.blit(self.surface, self.rect)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: (int, int, int) = (0, 0, 0)):
        self.__color = color
        self.surface.fill(color)
