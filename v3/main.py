'''
создать на экране несколько разных самолетиков
'''

import pygame
import view,controller

while True:
    controller.process_events()
    view.draw()
