import pygame

class Background:
    def __init__(self, image_path, screen):
        self.image = pygame.image.load(image_path)
        self.screen = screen
        # self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, (0, 0))
