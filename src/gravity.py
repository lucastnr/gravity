import pygame

size = width, height = 900, 800
# x = 2560 + 10
# y = (1080 - height) / 2
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

screen = pygame.display.set_mode(size)
pygame.init()

from objects.earth import earth
from objects.centralize_obj import centralize_object

mainLoop = True

while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

    screen.fill((0, 0, 0))
    centralize_object(earth)
    pygame.display.update()

pygame.quit()