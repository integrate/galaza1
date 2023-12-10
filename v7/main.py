'''
научить самолетики по команде перемещаться в определенную точку
'''

import pygame
import view,controller, model

while True:
    controller.process_events()
    model.step()
    view.draw()
