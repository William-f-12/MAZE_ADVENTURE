import pygame
from random import choice
location = r'.\all resource\\'
BASICFONT = pygame.font.Font('freesansbold.ttf', 20)

class Chest:

    def __init__(self, chest_info:dict):
        self._img = pygame.image.load(location + 'chest.png')
        self.rect = self._img.get_rect()
        self.rect.topleft = chest_info["pos"]
        self._buff = chest_info["buff"]
        self.buff_logo_pos = None
        self.is_opened = False


    def open(self, character):
        """player open the chest, give him buff"""

        self.is_opened = True
        self._buff.start(character)


    def draw(self, screen):
        """draw the chest on the screen"""

        screen.blit(self._img, self.rect)


    def show_logo(self, screen):
        """show buff logo"""

        if self._buff.img:
            self._buff.draw(screen, self.buff_logo_pos)

    
    def check(self, character, buff_logo_pos):
        """responsible for all things need to do in loop"""

        self.open(character)
        self.buff_logo_pos = buff_logo_pos


# ============== buff_list ================
from Buff import Intensified, Harden, Heal
intensify = Intensified() # damage boost
harden = Harden() # defense increased
heal = Heal() # healed

buff_list = [intensify, harden, heal]
# ============= chests ================
buff1 = choice(buff_list)
chest1 = {"pos":(912,224), "buff":buff1}

buff2 = choice(buff_list)
chest2 = {"pos":(656,128), "buff":buff2}

buff3 = choice(buff_list)
chest3 = {"pos":(640,336), "buff":buff3}

buff4 = choice(buff_list)
chest4 = {"pos":(288,432), "buff":buff4}

chests_list = (chest1, chest2, chest3, chest4)