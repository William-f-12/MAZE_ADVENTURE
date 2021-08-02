import pygame
location = r'.\all resource\\'

class Maze:

    def __init__(self, maze_list):
        self._maze_list = maze_list
        self._rect_list = []
        self._initialize_rect_lsit()


    def _initialize_rect_lsit(self):
        """initialize the rect list"""

        for m_local in self._maze_list:
            m_rect = pygame.Rect(m_local[0].get_rect())
            m_rect.topleft = (m_local[1], m_local[2])
            self._rect_list.append(m_rect)

    
    def draw(self, screen):
        """draw the maze"""

        for m_local in self._maze_list:
            screen.blit(m_local[0],(m_local[1],m_local[2]))
        

    def colliderect(self, player_rect):
        """detect the collision"""

        assert self._rect_list != [], "initialize the rect list before call colliderect"

        for m_rect in self._rect_list:
            if m_rect.colliderect(player_rect):  ##if the player collide the wall
                return True

        return False


# ================== MAZE 1 ==================
m1 = pygame.image.load(location + '1.png')
m2 = pygame.image.load(location + '2.png')
m3 = pygame.image.load(location + '3.png')
m4 = pygame.image.load(location + '4.png')
m5 = pygame.image.load(location + '5.png')
m6 = pygame.image.load(location + '6.png')
m7 = pygame.image.load(location + '7.png')
m8 = pygame.image.load(location + '8.png')
m9 = pygame.image.load(location + '9.png')
m10 = pygame.image.load(location + '10.png')
m11 = pygame.image.load(location + '11.png')
m12 = pygame.image.load(location + '12.png')
m13 = pygame.image.load(location + '13.png')
m14 = pygame.image.load(location + '14.png')
m15 = pygame.image.load(location + '15.png')
m16 = pygame.image.load(location + '16.png')
m17 = pygame.image.load(location + '17.png')
m18 = pygame.image.load(location + '18.png')
m19 = pygame.image.load(location + '19.png')
m20 = pygame.image.load(location + '20.png')
m21 = pygame.image.load(location + '21.png')
m22 = pygame.image.load(location + '22.png')
m23 = pygame.image.load(location + '23.png')
maze_list1 = [[m1,96,128],[m2,96,96],[m3,960,96],[m4,864,480],[m5,128,480],[m6,96,288],[m7,416,128],[m8,608,128],
             [m9,704,128],[m10,736,192],[m11,896,192],[m12,864,192],[m13,800,288],[m14,608,288],[m15,672,320],
             [m16,544,384],[m17,512,192],[m18,352,288],[m19,320,224],[m20,288,192],[m21,192,288],[m22,192,384],
             [m23,320,416]]
