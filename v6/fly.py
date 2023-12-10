import time

import pygame

pygame.init()

font_debug = pygame.font.SysFont("arial", 15)

class Fly:
    def __init__(self, image, step_image, size_multiply, x, y, step_speed=-5):

        self.main_image = pygame.image.load(image)
        self.main_image = pygame.transform.scale(self.main_image, [self.main_image.get_width() * size_multiply,
                                                                   self.main_image.get_height() * size_multiply])

        self.step_image = pygame.image.load(step_image)
        self.step_image = pygame.transform.scale(self.step_image, [self.step_image.get_width() * size_multiply,
                                                                   self.step_image.get_height() * size_multiply])

        self.rect = pygame.rect.Rect(x, y, self.main_image.get_width(), self.main_image.get_height())

        self._iam_on_step = False
        self._step_speed = step_speed

        self._current_angle = 0
        self._angle_step = 5
        self._target_angle = 0
        self._turn_timer = time.time()

        self.step_timer = time.time()

    def draw(self, screen: pygame.Surface):
        if not self._iam_on_step:
            image = self.main_image
        else:
            image = self.step_image
        image = pygame.transform.rotate(image, self._current_angle)
        image_rect = image.get_rect(center = self.rect.center)
        self.rect = image_rect

        screen.blit(image, image_rect)

    def draw_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)
        angle = font_debug.render("curr:"+ str(self._current_angle)+" tar:"+str(self._target_angle), True, [255,0,0])
        screen.blit(angle,[self.rect.x, self.rect.y-20])

    def _do_step(self):
        self._iam_on_step = not self._iam_on_step
        center = [self.rect.center[0], self.rect.center[1]]
        center[0] += self._step_speed
        if self._iam_on_step:
            self.rect.size = self.step_image.get_size()
        else:
            self.rect.size = self.main_image.get_size()
        self.rect.center = center

    def step(self):
        if time.time() - self.step_timer >= 0.5:
            self.step_timer = time.time()
            self._do_step()

        if time.time() - self._turn_timer>0.02:
            self._make_turn()
            self._turn_timer = time.time()

    def _make_turn(self):
        if self._target_angle<self._current_angle:
            self._current_angle-=self._angle_step
        elif self._target_angle>self._current_angle:
            self._current_angle+=self._angle_step

    def _turn_to(self, new_angle):
        self._target_angle = new_angle
