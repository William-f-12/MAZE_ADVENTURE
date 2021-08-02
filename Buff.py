import pygame
FPS = 30
location = r'.\all resource\\'

# =========== base class ============
class Buff:

    def __init__(self, duration):
        self._end_time = 0
        self._duration = duration # second
        self.is_affected = False
        self.img = None


    def start(self, time, character):
        """debuff starter"""

        self._end_time = time + self._duration * FPS
        self.is_affected = True
        self._affect_start(character)

    
    def _affect_start(self, character):
        """depends on different buff"""
        pass


    def _affect_end(self, character):
        """depends on different buff"""
        pass

    
    def end(self, character):
        """debuff ends"""

        self.is_affected = False
        self._affect_end(character)


    def timer(self, time, character):
        """check if debuff ends"""

        if time == self._end_time:
            self.end(character)

    
    def draw(self, screen, rect):
        """draw the sign on the screen"""
        # need to define self._img
        screen.blit(self.img, rect)


# =========== dizzy ===========
class Dizzy(Buff):

    def __init__(self, duration):
        self._end_time = 0
        self._duration = duration # second
        self.is_affected = False
        self.img = pygame.image.load(location + 'dizziness.png')
        self._dizzy_sound = pygame.mixer.Sound(location + 'warning.wav')
        self._dizzy_sound.set_volume(.2)


    def _affect_start(self, character):
        """stop character from moving"""

        character.can_move = False
        self._dizzy_sound.play()

    
    def _affect_end(self, character):
        """debuff ends, character can move"""

        character.can_move = True


# =========== intensified ============
class Intensified(Buff):

    def __init__(self):
        self.img = pygame.image.load(location + 'damage.png')


    def start(self, character):
        """intensify player's atk"""

        character.atk *= 2


# =========== Harden ============
class Harden(Buff):

    def __init__(self):
        self.img = pygame.image.load(location + 'defense.png')


    def start(self, character):
        """increase player's defense"""

        character.defense += 1.5


# =========== Heal ============
class Heal(Buff):

    def __init__(self):
        self.img = None


    def start(self, character):
        """heal player"""

        character.hp = min(100, character.hp+50)