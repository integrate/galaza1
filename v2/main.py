'''
Создайте на экране один самолет типа 1 и один типа 2
'''

import pygame
import view,controller

while True:
    controller.process_events()
    view.draw()