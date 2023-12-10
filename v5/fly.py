import time

import pygame.image


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

        self.step_timer = time.time()

    def draw(self, screen: pygame.Surface):
        if not self._iam_on_step:
            screen.blit(self.main_image, self.rect)
        else:
            screen.blit(self.step_image, self.rect)

    def draw_debug(self, screen: pygame.Surface):
        pygame.draw.rect(screen, [255, 0, 0], self.rect, 3)

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
