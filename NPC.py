import pygame
location = r'.\all resource\\'

class NPC:

    def __init__(self, npc_info:dict):
        self._img = npc_info["image"]
        self.rect = self._img.get_rect()
        self.rect.topleft = npc_info["pos"]
        self._need = npc_info["need"]
        self._need_num = npc_info["need number"]
        self.is_talk = False
        self._dialogue = npc_info["default dialogue"]
        self._dialogue2 = npc_info["dialogue 2"]
        self.quest = True


    def react(self, character):
        """rect with player"""

        if self.rect.colliderect(character.rect) and self.quest:
            self.is_talk = True
            if self._need in character.inventory:
                self._dialogue = self._dialogue2
                if character.is_attack:
                    self.quest = False
                    character.defense += 1
                    character.atk += 5
        else:
            self.is_talk = False


    def draw(self, screen):
        """draw the npc on the screen"""

        screen.blit(self._img, self.rect)
    

    def draw_dialogue(self, screen):
        """draw the dialogue on the screen"""

        if self.is_talk:
            screen.blit(self._dialogue, (48,360))


# =============== npc ================
npc_img = pygame.image.load(location + 'npc.png')
npc_react1 = pygame.image.load(location + 'npc_react1.png')
npc_react2 = pygame.image.load(location + 'npc_react2.png')
npc_info = {"image":npc_img,
            "pos":(1050,570),
            "need":"juice",
            "need number":1,
            "default dialogue":npc_react1,
            "dialogue 2":npc_react2}