from abc import ABC

import pygame


class AbstractPlayer(ABC):

    # General Atributes
    image = None
    rect = None

    # Stats
    damage = 0
    life = 0
    defense = 0
    speed = 0

    # Constructor
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.right = 1920 - self.rect.width
        self.rect.top = 1080 - self.rect.height

    # Methods
    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect

    def moveRigth(self):
        self.rect.x += self.speed

    def moveLeft(self):
        self.rect.x -= self.speed

    def moveDown(self):
        self.rect.y += self.speed

    def moveUp(self):
        self.rect.y -= self.speed

    def stop(self):
        self.rect.x = 0
        self.rect.y = 0

    def draw(self, window):
        window.blit(self.image, self.rect)

    def handle_events(self, key):
        if key == pygame.K_p:
            pygame.mixer.music.pause()
        elif key ==pygame. K_LEFT:
            self.moveLeft()
        elif key == pygame.K_RIGHT:
            self.moveRigth()
        elif key == pygame.K_UP:
            self.moveUp()
        elif key == pygame.K_DOWN:
            self.moveDown()
