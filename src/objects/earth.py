import pygame, sys
from src.utils.screen import screen_width, screen_height

from src.utils.physics import earth_proportion_screen

class Earth:
  def __init__(self):
    size = min(screen_width, screen_height) * earth_proportion_screen
    image = pygame.image.load("assets/textures/earth.png")
    self.__surface = pygame.transform.scale(image, (size, size))

  @property
  def surface(self):
    return self.__surface
  @property
  def rect(self):
    return self.__surface.get_rect()

earth = Earth()