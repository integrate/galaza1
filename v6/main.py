'''
научить самолетики по команде поворачиваться на произвольный угол
'''

import pygame
import view,controller, model

while True:
    controller.process_events()
    model.step()
    view.draw()
