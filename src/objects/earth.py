import pygame, sys
from src.utils.screen import screen_width, screen_height

if __name__ != "objects.earth":
    sys.exit()
class Earth:
  def __init__(self):
    size = min(screen_width, screen_height) / 5
    image = pygame.image.load("assets/textures/earth.png")
    self.__earth = pygame.transform.scale(image, (size, size))

  @property
  def earth(self):
    return self.__earth

earth = Earth().earth
rect = earth.get_rect()
