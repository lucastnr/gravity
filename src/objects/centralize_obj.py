from src.utils.screen import screen, screen_center_x, screen_center_y
from pygame import Surface

def centralize_object(surface: Surface):
  screen.blit(surface, (screen_center_x - surface.get_width() / 2,
                        screen_center_y - surface.get_height() / 2))
