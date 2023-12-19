import random

import pygame, model
def process_events():
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            exit()

        if e.type == pygame.KEYUP and e.key == pygame.K_TAB:
            model.debug_mode = not model.debug_mode

        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            model.fly1._turn_to(model.fly1._current_angle-90)
            model.fly2._turn_to(model.fly2._current_angle-180)
            model.fly3._turn_to(model.fly3._current_angle+25)

        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            # x = random.randint(100, 500)
            # y = random.randint(100, 500)
            # model.fly1.move_to_with_turn(x,y, 200)
            #
            # x = random.randint(100, 500)
            # y = random.randint(100, 500)
            # model.fly2.move_to_with_turn(x, y, 200)


            model.fly3.move_to_with_turn(x, y, 200)