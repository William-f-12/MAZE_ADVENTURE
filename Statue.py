import pygame
import random
location = r'.\all resource\\'

class Statue:

    def __init__(self, pos):
        self._img = pygame.image.load(location + "statue.png")
        self._rect = self._img.get_rect()
        self._rect.topleft = pos
        self.strange = pygame.image.load(location + 'strange.png')
        self.blessing1 = pygame.image.load(location + 'blessing1.png')
        self.blessing2 = pygame.image.load(location + 'blessing2.png')
        self.is_found = False
        self.can_bless = True


    def update(self, screen, collide_time, monsters:list, character):
        """check if player find the statue, and blessing the player"""

        if self._rect.colliderect(character.rect):
            self.is_found = True
            self.blessing(screen, character, collide_time, monsters)

    
    def draw(self, screen):
        """draw the statue on the screen"""

        if self.is_found:
            screen.blit(self._img, self._rect)


    def blessing(self, screen, character, collide_time, monsters:list):
        """blessing the character"""

        if self.can_bless:
            self.can_bless = False
            res = random.randint(1, 10)
            if res == 1:
                screen.blit(self.blessing1,(0,0))
                pygame.display.update()
                pygame.time.wait(3500)
                for monster in monsters:
                    monster.go_back = False
                    monster.atk = 100
            elif res == 2:
                screen.blit(self.blessing2,(0,0))
                pygame.display.update()
                pygame.time.wait(3500)
                character.atk = 1000
                collide_time = 9
            else:
                screen.blit(self.strange, (0,0))
                pygame.display.update()
                pygame.time.wait(3500)