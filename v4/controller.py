import pygame, model
def process_events():
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            exit()

        if e.type == pygame.KEYUP and e.key == pygame.K_TAB:
            model.debug_mode = not model.debug_mode
