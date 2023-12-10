import pygame.image


class Fly:
    def __init__(self, image,size_multiply,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [self.image.get_width()*size_multiply,self.image.get_height()*size_multiply])

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, [self.x,self.y])

