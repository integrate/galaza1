'''
сделайте перемещение самолета в указанную точку за указанное количество циклов с автоматческим поворотом на указанную точку
В ПРОЦЕССЕ
'''
import time

import pygame
import view,controller, model

while True:
    time.sleep(1/100)
    controller.process_events()
    model.step()
    view.draw()
