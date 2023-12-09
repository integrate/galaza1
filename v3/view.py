import pygame, model

display = pygame.display.set_mode([1000,1000])

def draw():
      display.fill([0,0,0])
      model.fly1.draw(display)
      model.fly2.draw(display)
      pygame.display.flip()
