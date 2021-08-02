import pygame
location = r'.\all resource\\'

class ITEM:

    def __init__(self, item_info:dict):
        self._img = item_info["img"]
        self._rect = self._img.get_rect()
        self._rect.topleft = item_info["pos"]
        self.name = item_info["name"]
        self.exist = True

    
    def react(self, character):
        """check it player pick the item"""

        if self._rect.colliderect(character.rect) and self.exist:
            character.inventory.append(self.name)
            self.exist = False


    def draw(self, screen):
        """draw the item on the screen"""

        if self.exist:
            screen.blit(self._img, self._rect)


# ========== juice ===========
juice_img = pygame.image.load(location + 'juice.png')
juice_info = {"img":juice_img,
              "pos":(8,108),
              "name":"juice"}