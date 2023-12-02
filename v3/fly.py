import pygame.image


class Fly:
    def __init__(self, image,w,h,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [w,h])

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, [self.x,self.y])

