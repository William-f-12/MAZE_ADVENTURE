import pygame
location = r'.\all resource\\'

class Character:

    def __init__(self, c_info:dict, WINDOWWIDTH, WINDOWHEIGHT):
        self.__character = c_info["img"]
        self.rect = pygame.Rect(928, 48, 32, 32) # 928, 48
        self.speed = c_info["speed"] #pixels per frame
        self.hp = c_info["hp"]
        self.atk = c_info["atk"]
        self.defense = c_info["defense"]
        self.inventory = []
        self.is_attack = False
        self.__face_direction = "left"
        self.can_move = True
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.__leftLimit = 16
        self.__rightLimit = WINDOWWIDTH - 16
        self.__upLimit = 16
        self.__downLimit = WINDOWHEIGHT - 16
        self.__pre_location = None

    
    @property
    def _img(self):
        """the image needed"""

        if self.__face_direction == "left":
            if self.is_attack and self.can_move:
                return self.__character["attack_left"]
            else:
                return self.__character["left"]
        elif self.__face_direction == "right":
            if self.is_attack and self.can_move:
                return self.__character["attack_right"]
            else:
                return self.__character["right"]

    
    def move(self):
        """make the character move"""

        if not self.can_move:
            return

        # left
        if self.left and self.rect.center[0] > self.__leftLimit:
            self.rect.left -= self.speed
            self.__face_direction = "left"
        # right
        if self.right and self.rect.center[0] < self.__rightLimit:
            self.rect.right += self.speed
            self.__face_direction = "right"
        # up
        if self.up and self.rect.center[1] > self.__upLimit:
            self.rect.top -= self.speed
        # down
        if self.down and self.rect.center[1] < self.__downLimit:
            self.rect.bottom += self.speed


    def record_pre_location(self):
        """record the pre-location"""

        self.__pre_location = self.rect.center


    def back_to_pre_location(self):
        """back to pre-location"""

        self.rect.center = self.__pre_location


    def attack(self, enemy):
        """character attack!"""
        
        if self.can_move:
            attack_rect = self._img.get_rect()
            attack_rect.center = self.rect.center
            if attack_rect.colliderect(enemy.rect):
                enemy.hp -= self.atk


    def draw(self, screen):
        """draw character on the screen"""

        rect = self._img.get_rect()
        rect.center = self.rect.center
        screen.blit(self._img, rect)


# ==================== wizard =========================
wizard_speed = 4
wizard_hp = 100
wizard_atk = 10
wizard_defense = 0
wizard_left = pygame.image.load(location + 'wizard.png')
wizard_right = pygame.transform.flip(wizard_left, True, False)
wizard_attack_left = pygame.image.load(location + 'wizard_attack.png')
wizard_attack_right = pygame.transform.flip(wizard_attack_left, True, False)
wizard_img = {"left": wizard_left, "right": wizard_right,
              "attack_left": wizard_attack_left, "attack_right": wizard_attack_right}
wizard = {"img": wizard_img, "speed": wizard_speed, "atk": wizard_atk, "defense": wizard_defense, "hp":wizard_hp}