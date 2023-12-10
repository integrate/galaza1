import pygame, model

display = pygame.display.set_mode([1000,1000])

def draw():
      display.fill([0,0,0])
      model.fly1.draw(display)
      model.fly2.draw(display)
      model.fly3.draw(display)
      if model.debug_mode:
            draw_debug()

      pygame.display.flip()


def draw_debug():
      model.fly1.draw_debug(display)
      model.fly2.draw_debug(display)
      model.fly3.draw_debug(display)