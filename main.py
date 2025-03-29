import pygame

pygame.init()
window = pygame.display.set_mode(size=(1024, 640))

while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pass
