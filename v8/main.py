'''
сделайте управление скоростью перемещения самолетиков через количество циклов
Например: 1 цикл - 0.1 секунды
При перемещении самолета можно указать, за сколько циклов он должен долететь до цели
'''

import pygame
import view,controller, model

while True:
    controller.process_events()
    model.step()
    view.draw()
