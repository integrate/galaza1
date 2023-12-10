'''
научить самолетики ходить вправо и влево с разной скоростью
'''

import pygame
import view,controller, model

while True:
    controller.process_events()
    model.step()
    view.draw()
