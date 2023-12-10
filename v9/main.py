'''
сделайте перемещение самолета в указанную точку за указанное количество циклов с автоматческим поворотом на указанную точку
В ПРОЦЕССЕ
'''

import pygame
import view,controller, model

while True:
    controller.process_events()
    model.step()
    view.draw()
