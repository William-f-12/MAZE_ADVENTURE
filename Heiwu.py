import pygame
location = r'.\all resource\\'

class Heiwu:

    def __init__(self):
        self._img = pygame.image.load(location + 'heiwu.png')
        self._rect = self._img.get_rect()
    

    def draw(self, screen, character):
        """draw the dark fog on the screen"""

        self._rect.center = character.rect.center
        screen.blit(self._img, self._rect)