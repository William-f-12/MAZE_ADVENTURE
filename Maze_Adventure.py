#! python3.8
# Maze_Adventure.py - to play the game!

import pygame, sys
from pygame.locals import *
pygame.init()

from Timer import Timer
from Buff import Dizzy
from Heiwu import Heiwu
from Statue import Statue
from Chest import Chest, chests_list
from Maze import Maze, maze_list1
from Character import Character, wizard
from Monster import Monster, monster_list
from NPC import NPC, npc_info
from QUEST_ITEM import ITEM, juice_info


FPS = 30
WINDOWWIDTH = 1088
WINDOWHEIGHT = 608
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Maze Adventure")
BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
LOCATION = r'.\all resource\\'


def main():
    start_screen()
    exitcode = play()
    end_screen(exitcode)


def play():
    ## set up
    FPSCLOCK = pygame.time.Clock()
    timer = Timer()
    # background
    background = pygame.image.load(LOCATION + 'background.png')
    # maze
    maze = Maze(maze_list1)
    # player character
    character = Character(wizard, WINDOWWIDTH, WINDOWHEIGHT)
    max_collide_time = 10
    # buff positions
    buff_pos_list = [(335, 20), (368, 20), (401, 20), (434, 20)]
    buff_pos_idx = 0
    # debuff
    dizzy_time = 1 #second
    dizzy = Dizzy(dizzy_time)
    # monster
    green_slime = Monster(monster_list["green_slime"])
    red_slime = Monster(monster_list["red_slime"])
    violet_slime = Monster(monster_list["violet_slime"])
    monsters = [green_slime,
                red_slime, 
                violet_slime]
    # chests
    chests = [Chest(chests_list[0]),
              Chest(chests_list[1]),
              Chest(chests_list[2]),
              Chest(chests_list[3])]
    # statue
    statue_pos = (736,128)
    statue = Statue(statue_pos)
    # npc
    npc = NPC(npc_info)
    # items
    juice = ITEM(juice_info)
    # heiwu
    heiwu = Heiwu()
    # bgm
    pygame.mixer.music.load(LOCATION + 'bgm.wav')
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(.15)

    ## game loop
    while True:
        ## event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                # check movement
                if event.key == K_a:
                    character.left = True
                if event.key == K_d:
                    character.right = True
                if event.key == K_w:
                    character.up = True
                if event.key == K_s:
                    character.down = True
                if event.key == K_p:
                    character.is_attack = True
            elif event.type == KEYUP:
                if event.key == K_a:
                    character.left = False
                if event.key == K_d:
                    character.right = False
                if event.key == K_w:
                    character.up = False
                if event.key == K_s:
                    character.down = False
                if event.key == K_p:
                    character.is_attack = False

        ## move and collision
        # record the pre-location in order to make the collision happens
        character.record_pre_location()
        # determine if can move
        if dizzy.is_affected:
            dizzy.timer(timer.time, character)
        # move
        character.move()
        monsters_move(monsters, character)
        # detect collision
        if maze.colliderect(character.rect):
            character.collide_times += 1
            character.back_to_pre_location()
            dizzy.start(timer.time, character)

        ## check attacking
        if character.is_attack:
            attack_monster(character, monsters)
        monsters_attack(monsters, character)

        ## check update
        # check monsters
        check_monster_lives(monsters)
        # check chests
        for chest in chests:
            if not chest.is_opened and chest.rect.colliderect(character.rect):
                chest.check(character, buff_pos_list[buff_pos_idx])
                if chest._buff.img:
                    buff_pos_idx += 1
        # check statue
        statue.update(DISPLAYSURF, monsters, character)
        # check npc
        npc.react(character)
        # check items
        juice.react(character)

        ## draw
        DISPLAYSURF.blit(background,(0,0))
        statue.draw(DISPLAYSURF)
        maze.draw(DISPLAYSURF)
        draw_monster(timer.time, monsters)
        character.draw(DISPLAYSURF)
        draw_chest(chests)
        if dizzy.is_affected:
            dizzy.draw(DISPLAYSURF, character.rect)
        npc.draw(DISPLAYSURF)
        juice.draw(DISPLAYSURF)
        heiwu.draw(DISPLAYSURF, character)
        npc.draw_dialogue(DISPLAYSURF)
        draw_HUD(character)
        draw_buff_logo(chests)

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        timer.count()

        # check if game ends
        if character.hp <= 0:
            pygame.mixer.music.stop()
            return "killed"
        if monsters == []:
            pygame.mixer.music.stop()
            return "win"
        if character.collide_times == max_collide_time:
            pygame.mixer.music.stop()
            return "injured"


def draw_HUD(character):
    show_health(character.hp)
    show_collide_times(character.collide_times)


def show_collide_times(collide_time):
    show_surf = BASICFONT.render("collision times: "+str(collide_time)+"/10", True, (255, 255, 255))
    show_rect = show_surf.get_rect()
    show_rect.topleft = (25, 50)
    DISPLAYSURF.blit(show_surf, show_rect)


def show_health(hp):
    # draw health bar
    health_bar1 = pygame.Rect(20, 20, 310, 30)
    health_bar2 = pygame.Rect(25, 25, 300, 20)
    pygame.draw.rect(DISPLAYSURF,(130, 130, 130), health_bar1)
    pygame.draw.rect(DISPLAYSURF,(255, 0, 0), health_bar2)
    # draw hp
    health = pygame.Rect(25, 25, 3*hp, 20) # default max hp is 100
    pygame.draw.rect(DISPLAYSURF,(0, 255, 0), health)


def monsters_attack(monsters, character):
    for monster in monsters:
        if monster.rect.colliderect(character.rect):
            monster.attack(character)


def monsters_move(monsters, character):
    for monster in monsters:
        monster.move(character)


def check_monster_lives(monsters):
    for monster in monsters:
        if monster.hp <= 0:
            monsters.remove(monster) # just use remove beacuse two monsters cannot die simultaneously


def draw_monster(time, monsters):
    for monster in monsters:
        monster.draw(DISPLAYSURF, time % 50 - 25)


def attack_monster(character, monsters):
    for monster in monsters:
        character.attack(monster)


def draw_chest(chests):
    for chest in chests:
        if not chest.is_opened:
            chest.draw(DISPLAYSURF)
        
def draw_buff_logo(chests):
    for chest in chests:
        if chest.is_opened:
            chest.show_logo(DISPLAYSURF)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    # background
    DISPLAYSURF.fill((60, 110, 200))
    title_surf = BASICFONT.render("MAZE ADVENTRUE", True, (0, 0, 0))
    title_rect = title_surf.get_rect()
    title_rect.center = (WINDOWWIDTH / 2, 250)
    DISPLAYSURF.blit(title_surf, title_rect)

    # narratage
    narratage1 = pygame.image.load(LOCATION + 'narratage1.png')
    narratage2 = pygame.image.load(LOCATION + 'narratage2.png')
    narratage3 = pygame.image.load(LOCATION + 'narratage3.png')
    narratage4 = pygame.image.load(LOCATION + 'narratage4.png')
    narratage_list = (narratage1, narratage2, narratage3, narratage4)
    narratage_idx = 0
    
    # while loop
    while True:
        # event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_p:
                    narratage_idx += 1
        
        # check ending condition
        if narratage_idx == 4:
            return

        # display intro
        DISPLAYSURF.blit(narratage_list[narratage_idx], (48,360))
        pygame.display.update()


def end_screen(exitcode):
    # show end screen
    if exitcode == "win":
        win_screen = pygame.image.load(LOCATION + 'win.png')
        DISPLAYSURF.blit(win_screen, (0, 0))
        pygame.display.update()
        win_sound = pygame.mixer.Sound(LOCATION + 'win.wav')
        win_sound.set_volume(.15)
        win_sound.play()
    elif exitcode == "killed":
        killed_screen = pygame.image.load(LOCATION + 'fail.png')
        DISPLAYSURF.blit(killed_screen, (0, 0))
        pygame.display.update()
        lose_sound = pygame.mixer.Sound(LOCATION + 'lose.wav')
        lose_sound.set_volume(.6)
        lose_sound.play()
    elif exitcode == "injured":
        injured_screen = pygame.image.load(LOCATION + 'commotio_cerebri.png')
        DISPLAYSURF.blit(injured_screen, (0, 0))
        pygame.display.update()
        lose_sound = pygame.mixer.Sound(LOCATION + 'lose.wav')
        lose_sound.set_volume(.6)
        lose_sound.play()
    pygame.time.wait(3000)

    # while loop
    while True:
        # event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()


# run! (>o<)!
if __name__ == "__main__":
    main()
