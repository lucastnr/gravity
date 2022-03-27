
import pygame
from objects.Movable import Moveable
from utils.physics import earth_size
from utils.screen import screen


class Circle(Moveable):
  radius = 0

  def __init__(self, radius: float):
    self.radius = radius
    super().__init__([450, 240], (8000, 0), (0, 0), 0)

  def render(self, paused: bool):
    if not paused:
      self.update_position()
    pygame.draw.circle(screen, (0, 255, 0),
                   self.position, self.radius)

  

circle = Circle(20)