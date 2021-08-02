import pygame, random as r, math, time  ##I googled how to use time: https://blog.csdn.net/leeafay/article/details/76409305
from pygame.locals import *
pygame.init()
width, height = 1088, 608  ##size of the window
screen = pygame.display.set_mode((width, height))

move = True
pre_local = [0,0]
collision = False
collide_timer = 0
dizziness_timer = 0
attack = False
attack_timer = 40  ##attack period
attack_timer_s = False
max_c = 10
timer1 = 0
wait = False

location = r'.\all resource\\'
####################################################  OTHER STUFF  ######################################################
chest_img = pygame.image.load(location + 'chest.png')
chest_list = [[912,224,True],[656,128,True],[640,336,True],[288,432,True]]
improvement = 0
hidden = pygame.image.load(location + 'hidden.png')
appear = False
statue_chance = True
r_num = r.randint(1,10)
blessing1 = pygame.image.load(location + 'blessing1.png')
blessing2 = pygame.image.load(location + 'blessing2.png')
strange = pygame.image.load(location + 'strange.png')
clue1_img = pygame.image.load(location + 'clue.png')
clue2_img = pygame.image.load(location + 'clue2.png')
dizziness = pygame.image.load(location + 'dizziness.png')
heiwu_img = pygame.image.load(location + 'heiwu.png')
background = pygame.image.load(location + 'background.png')
healthbar = pygame.image.load(location + 'healthbar.png')
health = pygame.image.load(location + 'health.png')
fail = pygame.image.load(location + 'fail.png')
win = pygame.image.load(location + 'win.png')
commotio_cerebri = pygame.image.load(location + 'commotio_cerebri.png')
damage_img = pygame.image.load(location + 'damage.png')
defense_img = pygame.image.load(location + 'defense.png')
d2_img = pygame.image.load(location + 'd2.png')
buff_damage = 0
buff_defense = 0
d2 = False
narratage1 = pygame.image.load(location + 'narratage1.png')
narratage2 = pygame.image.load(location + 'narratage2.png')
narratage3 = pygame.image.load(location + 'narratage3.png')
narratage4 = pygame.image.load(location + 'narratage4.png')
n = 1
juice_img = pygame.image.load(location + 'juice.png')
getjuice = pygame.image.load(location + 'getjuice.png')
juice = True
juice1 = False
#####################################################  CHARACTER  ########################################################
wizard1_img = pygame.image.load(location + 'wizard.png')
wizard2_img = pygame.transform.flip(wizard1_img, True, False)
wizard1_attack_img = pygame.image.load(location + 'wizard_attack.png')
wizard2_attack_img = pygame.transform.flip(wizard1_attack_img, True, False)
wizard_img = wizard1_img
wizard_attack_img = wizard1_attack_img
player_speed = 4
player_health = 100
player_atk = 10
player_up = False
player_down = False
player_left = False
player_right = False
player_x = 912  ##(928,48)
player_y = 32
npc = pygame.image.load(location + 'npc.png')
npc_react1 = pygame.image.load(location + 'npc_react1.png')
npc_react2 = pygame.image.load(location + 'npc_react2.png')
npc_react3 = pygame.image.load(location + 'npc_react3.png')
react = True
react1 = False
react2 = False
##################################################  MONSTER  ########################################################
slime_g1 = pygame.image.load(location + 'slime_g1.png')
slime_g2 = pygame.image.load(location + 'slime_g2.png')
slime_r1 = pygame.image.load(location + 'slime_r1.png')
slime_r2 = pygame.image.load(location + 'slime_r2.png')
slime_v1 = pygame.image.load(location + 'slime_v1.png')
slime_v2 = pygame.image.load(location + 'slime_v2.png')
slime_notice = pygame.image.load(location + 'slime_notice.png')
slime_list = [[768,384],[192,192],[416,384]]
slime_infor = [[800,2,2],[500,4,1],[1000,8,4]]
range_list = [[704,320],[128,128],[352,320]]
limit = True
def slime_back(range_x,range_y):  ##when player go out of slime's attack range, slime go back
    if slime_list[s_local][0] > range_x:
        slime_list[s_local][0] -= slime_infor[s_local][2]
    elif slime_list[s_local][0] < range_x:
        slime_list[s_local][0] += slime_infor[s_local][2]
    if slime_list[s_local][1] > range_y:
        slime_list[s_local][1] -= slime_infor[s_local][2]
    elif slime_list[s_local][1] < range_y:
        slime_list[s_local][1] += slime_infor[s_local][2]
###################################################  MAZE  ##########################################################
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
maze_list = [[m1,96,128],[m2,96,96],[m3,960,96],[m4,864,480],[m5,128,480],[m6,96,288],[m7,416,128],[m8,608,128],\
             [m9,704,128],[m10,736,192],[m11,896,192],[m12,864,192],[m13,800,288],[m14,608,288],[m15,672,320],\
             [m16,544,384],[m17,512,192],[m18,352,288],[m19,320,224],[m20,288,192],[m21,192,288],[m22,192,384],\
             [m23,320,416]]
####################################################  Music  ##########################################################
##the websites I used: https://www.pygame.org/docs/ref/music.html and https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound
pygame.mixer.music.load(location + 'bgm.wav')  ##by 
pygame.mixer.music.play(-1,0.0)  ##tells the user how many timws to play and when to end
pygame.mixer.music.set_volume(.15)
win_sound = pygame.mixer.Sound(location + 'win.wav')
lose_sound = pygame.mixer.Sound(location + 'lose.wav')
warning = pygame.mixer.Sound(location + 'warning.wav')
hit = pygame.mixer.Sound(location + 'hit.wav')
gethit = pygame.mixer.Sound(location + 'gethit.wav')
statue_sound = pygame.mixer.Sound(location + 'statue.wav')
buff_sound = pygame.mixer.Sound(location + 'buff.wav')
win_sound.set_volume(.15)
lose_sound.set_volume(.6)
warning.set_volume(.2)
hit.set_volume(.5)
gethit.set_volume(.1)
statue_sound.set_volume(.5)
buff_sound.set_volume(.3)
#######################################################################################################################

running = True
exitcode = 0
font = pygame.font.Font(None,20)
while running:
    timer1 += 1    
    screen.blit(background,(0,0))  ##background
##create player rect
    player_rect = pygame.Rect(wizard_img.get_rect())
    player_rect.top = player_y
    player_rect.left = player_x
##let images move
    if math.sin(timer1 / 5) >= 0:  ##just think there may be a sine in the math
        slime_g = slime_g1
        slime_r = slime_r1
        slime_v = slime_v1
        clue_img = clue1_img
    else:
        slime_g = slime_g2
        slime_r = slime_r2
        slime_v = slime_v2
        clue_img = clue2_img
    slime = [slime_g,slime_r,slime_v]
##juice
    juice_rect = pygame.Rect(juice_img.get_rect())
    juice_rect.top = 8
    juice_rect.left = 8
    if juice == True:
        screen.blit(juice_img,(8,8))
        if juice_rect.colliderect(player_rect):
            juice = False
            juice1 = True
            buff_sound.play()
            wait = True
##npc
    screen.blit(npc,(1050,570))
    npc_rect = pygame.Rect(juice_img.get_rect())
    npc_rect.top = 570
    npc_rect.left = 1050
    if npc_rect.colliderect(player_rect):
        if react == True:
            if juice == True:
                react1 = True
            elif juice == False:
                react2 = True
    else:
        react1 = False
        react2 = False
##clue
    screen.blit(clue_img,(608,416))
    clue_rect = pygame.Rect(clue_img.get_rect())
    clue_rect.top = 416
    clue_rect.left = 608          
##game ending conditions
    if player_health <= 0:  ##when player die
        running = False
        exitcode = 0
    elif slime_infor[0][0] <= 0 and slime_infor[1][0] <= 0 and slime_infor[2][0] <= 0 \
       and player_rect.colliderect(clue_rect):  ##when player find the clue and beat 3 slimes
        running = False
        exitcode = 1
    elif collide_timer >= max_c:  ##usually, player can collide with the wall 10 times at most in a single game
        running = False
        exitcode = 2
##build maze
    for m_local in maze_list:
        screen.blit(m_local[0],(m_local[1],m_local[2]))
        m_rect = pygame.Rect(m_local[0].get_rect())
        m_rect.top = m_local[2]
        m_rect.left = m_local[1]
        if m_rect.colliderect(player_rect):  ##if the player collide the wall
            collision = True
            move = False
##put slime in the maze
    for s_local in range(len(slime_list)):
        if slime_infor[s_local][0] > 0:
            screen.blit(slime_notice,(range_list[s_local][0],range_list[s_local][1]))
            notice_range = pygame.Rect(slime_notice.get_rect())
            notice_range.top = range_list[s_local][1]
            notice_range.left = range_list[s_local][0]
            if notice_range.colliderect(player_rect):
                if player_x > slime_list[s_local][0]:
                    slime_list[s_local][0] += slime_infor[s_local][2]
                elif player_x < slime_list[s_local][0]:
                    slime_list[s_local][0] -= slime_infor[s_local][2]
                if player_y > slime_list[s_local][1]:
                    slime_list[s_local][1] += slime_infor[s_local][2]
                elif player_y < slime_list[s_local][1]:
                    slime_list[s_local][1] -= slime_infor[s_local][2]
            else:  ##ensure the fairness of the game
                if s_local == 0 and limit == True:
                    slime_back(768,384)
                elif s_local == 1 and limit == True:
                    slime_back(192,192)
                elif s_local == 2 and limit == True:
                    slime_back(416,384)
            screen.blit(slime[s_local],(slime_list[s_local][0],slime_list[s_local][1]))
            if s_local == 0:
                slime_health = font.render(str(slime_infor[0][0]) + '/800',True,(255,255,255))
                screen.blit(slime_health,(slime_list[0][0],slime_list[0][1] - 15))
            elif s_local == 1:
                slime_health = font.render(str(slime_infor[1][0]) + '/500',True,(255,255,255))
                screen.blit(slime_health,(slime_list[1][0],slime_list[1][1] - 15))
            elif s_local == 2:
                slime_health = font.render(str(slime_infor[2][0]) + '/1000',True,(255,255,255))
                screen.blit(slime_health,(slime_list[2][0],slime_list[2][1] - 15))        
##chests
    for c_local in chest_list:  ##c_local is list
        screen.blit(chest_img,(c_local[0],c_local[1]))  ##build chests
        chest_range = pygame.Rect(chest_img.get_rect())
        chest_range.top = c_local[1]
        chest_range.left = c_local[0]
        if player_rect.colliderect(chest_range):  ##when player find the chest
            if c_local[2] == True:
                improvement = r.randint(1,3)
                c_local[2] = False
                if improvement == 1:  ##player_atk up
                    player_atk *= 2
                    improve = font.render('Damage boost',True,(255,0,0))
                    buff_damage += 1
                elif improvement == 2:  ##player get healed
                    player_health += 50
                    if player_health > 100:
                        player_health = 100
                    improve = font.render('Healed',True,(0,255,0))
                elif improvement == 3:  ##player's defense boost
                    for s_atk in slime_infor:
                        if s_atk[1] != 0:
                            s_atk[1] -= 1
                    improve = font.render('Defense boost',True,(0,0,255))
                    buff_defense += 1
                screen.blit(improve,(player_x,player_y - 15))  ##display infor
                buff_sound.play()
                wait = True
##save the pre_local infor
    if collision == False:  
        pre_local[0] = player_x
        pre_local[1] = player_y
##player attack
    if attack == True and move == True:  ##image of attacking
        screen.blit(wizard_attack_img,(player_x - 15,player_y - 15))
        attack_range = pygame.Rect(wizard_attack_img.get_rect())  ##attack range
        attack_range.top = player_y - 15
        attack_range.left = player_x - 15
        for slime_hit in slime:
            slime_rect = pygame.Rect(slime_hit.get_rect())
            slime_rect.top = slime_list[slime.index(slime_hit)][1]
            slime_rect.left = slime_list[slime.index(slime_hit)][0]
            if slime_rect.colliderect(attack_range):  ##if attack hit slime
                slime_infor[slime.index(slime_hit)][0] -= player_atk
        if attack_timer == 31:  ##showing time of the image of attack is 10
            attack = False
    else:
        screen.blit(wizard_img,(player_x,player_y))
##slime attak
    for slime_hit in slime:  ##when slime hit player
        slime_rect = pygame.Rect(slime_hit.get_rect())
        slime_rect.top = slime_list[slime.index(slime_hit)][1]
        slime_rect.left = slime_list[slime.index(slime_hit)][0]
        if slime_rect.colliderect(player_rect) and slime_infor[slime.index(slime_hit)][0] > 0:
            player_health -= slime_infor[slime.index(slime_hit)][1]
            gethit.play()
##statue 
    if appear == False:  ##the statue appear
        screen.blit(hidden,(736,128))
    hidden_rect = pygame.Rect(hidden.get_rect())
    hidden_rect.top = 128
    hidden_rect.left = 736
   
    if hidden_rect.colliderect(player_rect):  ##when player find the hidden operating statue
        appear = True
        if statue_chance == True:  ##when player react with the operation statue
            statue_sound.play()
            while statue_chance == True:
                player_up = False
                player_down = False
                player_left = False
                player_right = False
                if r_num == 1 or r_num == 2:                
                    if r_num == 1:
                        screen.blit(blessing1,(0,0))  ##blessing1
                        limit = False  ##slime will not go back
                        for atk in slime_infor:  ##slime become strong
                            atk[1] = 100
                    elif r_num == 2:
                        screen.blit(blessing2,(0,0))  ##blessing2
                        player_atk = 1000  ##player because strong
                        max_c = 1  ##player can collide with the wall once
                        collide_timer = 0
                else:
                    screen.blit(strange,(0,0))  ##nothing happen
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  ##quit the game
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_p:  ##press p to continue
                            statue_chance = False  ##can only recat once
                pygame.display.update()  ##screen update
##dizziness
    if dizziness_timer > 0:
        screen.blit(dizziness,(player_x,player_y))  ##image of dizziness sign
##heiwu
    if running == True:
        screen.blit(heiwu_img,(player_x - 1284,player_y - 1284))
##attack priod
    if attack_timer_s == True:  ##when an attack starts, count its period
        attack_timer -= 1
        if attack_timer == 0:
            attack_timer = 40
            attack_timer_s = False
##health bar
    screen.blit(healthbar,(50,20))  
    for h in range(player_health):  ##health of player
        screen.blit(health,(50 + h * 3,20))
    hit_wall_times = font.render('collision times: ' + str(collide_timer) + '/' + str(max_c),True,(255,255,255))
    screen.blit(hit_wall_times,(50,55))
##buff
    for buff1 in range(buff_damage):
        screen.blit(damage_img,(355 + buff1 * 33,20))
    for buff2 in range(buff_defense):
        screen.blit(defense_img,(355 + buff2 * 33,55))
    if d2 == True:
        screen.blit(d2_img,(322,55))
##react with npc/juice
    if juice1 == True:
        screen.blit(getjuice,(48,360))
        juice1 = False
    if react1 == True:
        screen.blit(npc_react1,(48,360))
    elif react2 == True:
        screen.blit(npc_react2,(48,360))
##screen update    
    pygame.display.update()  
    if wait == True:
        time.sleep(2)
        wait = False
##introduction of the game
    while timer1 == 1:
        if n == 1:
            screen.blit(narratage1,(48,360))
        elif n == 2:
            screen.blit(narratage2,(48,360))
        elif n == 3:
            screen.blit(narratage3,(48,360))
        elif n == 4:
            screen.blit(narratage4,(48,360))
        elif n == 5:
            timer1 = 2
        pygame.display.update()  ##screen update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  ##quit the game
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_p:  ##press p to continue
                    n += 1
##event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  ##quit the game
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  ##key down
            if event.key == K_p:  ##attack
                if attack_timer == 40:
                    attack = True
                    attack_timer_s = True
                    hit.play()
                    if react2 == True:  ##when player give the juice to ninja
                        react = False
                        react2 = False
                        d2 = True
                        player_atk += 5
                        for s_atk in slime_infor:
                            if s_atk[1] != 0:
                                s_atk[1] -= 1
                        screen.blit(npc_react3,(48,360))
                        pygame.display.update()
                        buff_sound.play()
                        time.sleep(2)

            if event.key == K_w:
                player_up = True
            elif event.key == K_a:
                player_left = True
            elif event.key == K_s:
                player_down = True
            elif event.key == K_d:
                player_right = True

        if event.type == KEYUP:  ##key up
            if event.key == K_p:
                attack = False

            if event.key == K_w:
                player_up = False
            elif event.key == K_a:
                player_left = False
            elif event.key == K_s:
                player_down = False
            elif event.key == K_d:
                player_right = False

    if move == True:
        ##movement up and down and build the wall 
        if player_up == True:
            player_y -= player_speed
        elif player_down == True:
            player_y += player_speed

        ##movement right and left
        if player_left == True:
            wizard_img = wizard1_img
            wizard_attack_img = wizard1_attack_img  ##player turn left
            player_x -= player_speed
        elif player_right == True:
            wizard_img = wizard2_img
            wizard_attack_img = wizard2_attack_img  ##player turn right
            player_x += player_speed

    ##limite of map
    if player_x <= 0:
        player_x = 0
    elif player_x >= 1056:
        player_x = 1056
    if player_y <= 0:
        player_y = 0
    elif  player_y >= 576:
        player_y = 576
##make sure plyer don't stay in walls
    if collision == True:  
        player_x = pre_local[0]
        player_y = pre_local[1]
##dizziness
    dizziness_timer -= 1
    if collision == True:
        warning.play()
        collide_timer += 1
        dizziness_timer = 20  ##when player collide with the wall, he can't move for a while
    if dizziness_timer <= 0:
        move = True
    collision = False

pygame.mixer.music.stop()
gethit.stop()
hit.stop()
warning.stop()
##won or lost
if exitcode == 0:
    screen.blit(fail,(0,0))
    lose_sound.play()
elif exitcode == 1:
    screen.blit(win,(0,0))
    win_sound.play()
elif exitcode == 2:
    screen.blit(commotio_cerebri,(0,0))
    lose_sound.play()
pygame.display.update()  ##screen update
##player leave
while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  ##quit the game
            pygame.quit()
            exit()
