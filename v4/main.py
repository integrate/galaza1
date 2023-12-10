'''
сделать самолетикам плавное движение вправо со сменой костюмов. микро движение каждые 0.5 секунд
'''

import pygame
import view,controller, model

while True:
    controller.process_events()
    model.step()
    view.draw()
