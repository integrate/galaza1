'''
создать на экране несколько рядов самолетов
для создания рядов из самолетов нужно владение range - пройти курс iterable course
'''

import pygame
import view,controller

while True:
    controller.process_events()
    view.draw()
