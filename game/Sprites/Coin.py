import pygame
from game.Sprite import Sprite


class Coin(Sprite):

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)
