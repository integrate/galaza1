import pygame
def process_events():
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            exit()