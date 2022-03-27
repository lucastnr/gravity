import pygame
import os

size = width, height = 900, 900
x = 2560 # - 960
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

screen = pygame.display.set_mode(size)
pygame.init()


from objects.earth import earth
from objects.circle import circle
from objects.centralize_obj import centralize_surface

mainLoop = True
paused = False

while mainLoop:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        mainLoop = False
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        paused = not paused
  screen.fill((0, 0, 0))
  circle.render(paused)
  centralize_surface(earth.surface)
  pygame.display.update()

pygame.quit()