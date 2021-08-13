import pygame
location = r'.\all resource\\'

class Monster:

    def __init__(self, m_info: dict):
        self._img_list = (m_info["img1"], m_info["img2"])
        self.rect = self._img_list[0].get_rect()
        self.inital_pos = m_info["pos"]
        self.rect.topleft = m_info["pos"]
        self.speed = m_info["speed"]
        self.hp = m_info["hp"]
        self._max_hp = m_info["hp"]
        self.atk = m_info["atk"]
        self._notice_range = m_info["notice_range"]
        self._range_rect = self._notice_range.get_rect()
        self._range_rect.topleft = m_info["range_pos"]
        self.go_back = True


    def move(self, character):
        """the simple ai determine the monster's movement"""

        # if player in attack range, chase the player
        if self._range_rect.colliderect(character.rect):
            if character.rect.left != self.rect.left:
                factor = (character.rect.left-self.rect.left)/abs(character.rect.left-self.rect.left)
                self.rect.left += self.speed * factor
            if character.rect.top != self.rect.top:
                factor = (character.rect.top-self.rect.top)/abs(character.rect.top-self.rect.top)
                self.rect.top += self.speed * factor
        # if player not in attack range, back to inital position
        else:
            # unless...
            if self.go_back:
                if self.rect.left != self.inital_pos[0]:
                    factor = (self.inital_pos[0]-self.rect.left)/abs(self.inital_pos[0]-self.rect.left)
                    self.rect.left += self.speed * factor
                if self.rect.top != self.inital_pos[1]:
                    factor = (self.inital_pos[1]-self.rect.top)/abs(self.inital_pos[1]-self.rect.top)
                    self.rect.top += self.speed * factor


    def attack(self, character):
        """monster attack the player!"""

        character.hp -= max(0, (self.atk - character.defense))


    def show_health(self, screen):
        """show monster's hp above it"""

        # draw health bar
        health_bar = pygame.Rect(self.rect.left, self.rect.top-5, 32, 4)
        pygame.draw.rect(screen,(255, 0, 0), health_bar)
        # draw hp
        health = pygame.Rect(self.rect.left, self.rect.top-5, 32*self.hp/self._max_hp, 4) # default max hp is 100
        pygame.draw.rect(screen,(0, 255, 0), health)


    def draw(self, screen, state: int):
        """draw the monster on the screen"""

        # draw the range
        screen.blit(self._notice_range, self._range_rect)
        # draw the monster
        if state > 0:
            img = self._img_list[0]
        else:
            img = self._img_list[1]
        screen.blit(img, self.rect)
        self.show_health(screen)



notice_range = pygame.image.load(location + 'slime_notice.png')
# ============= green slime ===============
slime_g1 = pygame.image.load(location + 'slime_g1.png')
slime_g2 = pygame.image.load(location + 'slime_g2.png')
green_slime = {"hp": 800, "atk": 2, "speed": 2,
               "img1": slime_g1, "img2": slime_g2, "pos": [768,384],
               "notice_range": notice_range, "range_pos": [704,320]}

# =============== red slime ===============
slime_r1 = pygame.image.load(location + 'slime_r1.png')
slime_r2 = pygame.image.load(location + 'slime_r2.png')
red_slime = {"hp": 500, "atk": 4, "speed": 1, 
             "img1": slime_r1, "img2": slime_r2, "pos": [192,192],
             "notice_range": notice_range, "range_pos": [128,128]}

# =============== violet slime ==============
slime_v1 = pygame.image.load(location + 'slime_v1.png')
slime_v2 = pygame.image.load(location + 'slime_v2.png')
violet_slime = {"hp": 1000, "atk": 8, "speed": 4,
                "img1": slime_v1, "img2": slime_v2, "pos": [416,384],
                "notice_range": notice_range, "range_pos": [352,320]}

# ================== monster list ==================
monster_list = {
                "green_slime": green_slime,
                "red_slime": red_slime,
                "violet_slime": violet_slime,
                }