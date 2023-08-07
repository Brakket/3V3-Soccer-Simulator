import pygame
from goal import Goal
from ballclassic import Ball
from players import Player
import random
pygame.init() #pygame initialization
import time

size = (700, 500)
screen = pygame.display.set_mode(size)
from time import sleep

#colors
Black = (0,0,0)
White = (255,255,255)
Red = (122.5,0,0)
Blue = (0,0,122.5)
Green = (0,122.5,0)
Yellow = (122.5,122.5,0)
bbBlue = (0,10,225)
Grey = (200,200,200)
DGrey = (150,150,150)

#Goal
goal1 = Goal(Black, 10, 100)
goal1.rect.x = 10
goal1.rect.y = 200

goal2 = Goal(Black, 10, 100)
goal2.rect.x = 680
goal2.rect.y = 200

#Ball
ball = Ball(Black,20,20)
ball.rect.x = 345
ball.rect.y = 195

#Players
all_players_list = pygame.sprite.Group()
player0 = Player(Red,80,230)
player1 = Player(Red,280,100)
player2 = Player(Red,280,375)
player3 = Player(Blue,580,230)
player4 = Player(Blue,390,100)
player5 = Player(Blue,390,375)
all_players_list.add(player0)
all_players_list.add(player1)
all_players_list.add(player2)
all_players_list.add(player3)
all_players_list.add(player4)
all_players_list.add(player5)
Team1 = pygame.sprite.Group()
Team1.add(player0)
Team1.add(player1)
Team1.add(player2)
Team2 = pygame.sprite.Group()
Team2.add(player3)
Team2.add(player4)
Team2.add(player5)

count = 1




#Sprites
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(goal1)
all_sprites_list.add(goal2)
all_sprites_list.add(ball)
all_sprites_list.add(player0)
all_sprites_list.add(player1)
all_sprites_list.add(player2)
all_sprites_list.add(player3)
all_sprites_list.add(player4)
all_sprites_list.add(player5)



#Window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("3v3 Soccer")

#fonts
font = pygame.font.Font(None, 45)
scorefont = pygame.font.Font(None, 74)
bigfont = pygame.font.Font(None, 100)
font1 = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 75)
smalltext = pygame.font.Font(None, 25)
finfont = pygame.font.Font(None,45)
minitext = pygame.font.Font(None,25)

#loop
startMenu = True
screenUpdate = pygame.time.Clock()

#Score
score1 = 0
score2 = 0

while(startMenu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            startMenu = False
            options = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        screen.fill(Green)
        intr1=bigfont.render("3v3",300,White)
        screen.blit(intr1,(150,25))
        intr2=smalltext.render("CREATED BY: MIRKO MICHOVICH + SEGUN MADARIKAN",300, Black)
        screen.blit(intr2,(150,100))
        pygame.draw.line(screen,White, [349, 0],[349, 500], 5)
        pygame.draw.rect(screen,Black, pygame.Rect(0,0,700,500),15)
        pygame.draw.rect(screen,White, pygame.Rect(15,15,670,470),5)

        pygame.draw.rect(screen,White, pygame.Rect(0,199,20,100))#goal
        pygame.draw.rect(screen,White, pygame.Rect(680,199,20,100))#goal

        pygame.draw.circle(screen,White,[349,249],75,5)
        pygame.display.update()
        screenUpdate.tick(60)

while(options):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                options = False
                spectate = True
                play = False
            if event.key == pygame.K_2:
                options = False
                spectate = False
                play = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        screen.fill(Green)
        screen.blit(intr1,(150,25))
        screen.blit(intr2,(150,100))
        subx=font.render("Score the most goals to WIN!",300,White)
        screen.blit(subx,(170,130))
        sub1=font.render("Press 1 to SPECTATE",300,White)
        screen.blit(sub1,(170,180))
        sub2=font.render("Press 2 to PLAY",300,White)
        screen.blit(sub2,(170,230))
        sub4 = font.render("Press ESC to QUIT", 300, White)
        screen.blit(sub4, (170,330))
        pygame.display.update()
        screenUpdate.tick(60)
    #Time measurements for possesion
    timeR = 0
    timeB = 0
    redHasBall = False
    blueHasBall = False

while spectate:
    if blueHasBall == True:
        timeB = 2.1
    if redHasBall == True:
        timeR = 2.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spectate = False
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            while True:
                screen.fill(White)
                event = pygame.event.wait()
                pausetext = font2.render("PAUSED",250,Black)
                conttext = font1.render("Press p to CONTINUE", 200, Black)
                quittext = font1.render("Press ESC to QUIT",200,Black)

                scr2text = scorefont.render(str(score2), 1, Blue)
                scr1text = scorefont.render(str(score1), 1, Red)

                screen.blit(pausetext,(250,150))
                screen.blit(conttext,(255,210))
                pygame.display.flip()
                if event.type == pygame.QUIT:
                    gameOn = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    break
                if event.type == pygame.K_ESCAPE:
                    gameOn = False
                    pygame.QUIT
                    quit()
    keys = pygame.key.get_pressed()
    #Kick control to the right need to fix this depending 

 # Score
    score1text = scorefont.render(str(score1), 1, Black)
    screen.blit(score1text, (250,10))
    score2text = scorefont.render(str(score2), 1, Black)
    screen.blit(score2text, (420,10))
#Grid variables
    Fieldstartx = 15
    Fieldstarty = 15
    boxWidth = 163.75
    boxHeight = 227.5
#Ball guards
    if ball.rect.y>490 or ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    if ball.rect.x>685 or ball.rect.x<5: #if ball goes to the right 
        ball.velocity[0] = -ball.velocity[0]
#Player guards
    for i in all_players_list:
        if i.rect.y>Fieldstarty+boxHeight*2 or i.rect.y<Fieldstarty:
            i.velocity[1] = -i.velocity[1]

        if i.rect.x>Fieldstartx+boxWidth*4-20 or i.rect.x<Fieldstartx+20: #if i goes to the right 
            i.velocity[0] = -i.velocity[0]
#GoalKeeperRed
    def GKR():
        global redHasBall
        global timeR
        if redHasBall == False:
            if ball.rect.x <= (Fieldstartx + boxWidth):
                if not player0.rect.y == ball.rect.y + 8:
                    if player0.rect.y < ball.rect.y + 8:
                        player0.rect.y += 2
                    elif  player0.rect.y > ball.rect.y - 43:
                        player0.rect.y -= 2
                else:
                    player0.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight*2):
                if not player0.rect.x == ball.rect.x + 8:
                    if player0.rect.x < ball.rect.x + 8:
                        player0.rect.x += 2
                    elif  player0.rect.x > ball.rect.x - 43:
                        player0.rect.x -= 2
                else:
                    player0.rect.x == ball.rect.x + 8    
            if player0.rect.x >= Fieldstartx + boxWidth: player0.rect.x = Fieldstartx + boxWidth
            elif player0.rect.x <= Fieldstartx: player0.rect.x = Fieldstartx
            if player0.rect.y >= 470: player0.rect.y = 470
            elif player0.rect.y <= Fieldstarty: player0.rect.y = Fieldstarty
        if redHasBall == True:
                    guess = random.uniform(2,15)
                    if timeR >= guess:
                        ball.shootRight()
                        ball.update()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        redHasBall = False
                        timeR = 0
    GKR()
#Player1Red
    def OffensiveP1R():
        global redHasBall
        global timeR
        if redHasBall == False:
            if ball.rect.x >= (Fieldstartx + boxWidth*2):
                if not player1.rect.y == ball.rect.y + 8:
                    if player1.rect.y < ball.rect.y + 8:
                        player1.rect.y += 2
                    elif  player1.rect.y > ball.rect.y - 43:
                        player1.rect.y -= 2
                else:
                    player1.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight):
                if not player1.rect.x == ball.rect.x + 8:
                    if player1.rect.x < ball.rect.x + 8:
                        player1.rect.x += 2
                    elif  player1.rect.x > ball.rect.x - 43:
                        player1.rect.x -= 2
                else:
                    player1.rect.x == ball.rect.x + 8    
            if player1.rect.x >= Fieldstartx+boxWidth*4-40: player1.rect.x = Fieldstartx+boxWidth*4-40
            elif player1.rect.x <= Fieldstartx + boxWidth*2: player1.rect.x = Fieldstartx + boxWidth*2
            if player1.rect.y >= Fieldstarty + boxHeight: player1.rect.y = Fieldstarty + boxHeight
            elif player1.rect.y <= Fieldstarty: player1.rect.y = Fieldstarty 

        if redHasBall == True:
                    guess = random.uniform(2,15)
                    if timeR >= guess:
                        accuracy = random.randint(1,3)
                        if accuracy > 1:
                            ball.shootRight()
                        else: ball.finishRight()
                        ball.update()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        redHasBall = False
                        timeR = 0
    def DefensiveP1R():
        global redHasBall
        global timeR
        if redHasBall == False:
            if ball.rect.x >= (Fieldstartx + boxWidth) and ball.rect.x <= (Fieldstartx + boxWidth*2):
                if not player1.rect.y == ball.rect.y + 8:
                    if player1.rect.y < ball.rect.y + 8:
                        player1.rect.y += 2
                    elif  player1.rect.y > ball.rect.y - 43:
                        player1.rect.y -= 2
                else:
                    player1.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight*2):
                if not player1.rect.x == ball.rect.x + 8:
                    if player1.rect.x < ball.rect.x + 8:
                        player1.rect.x += 2
                    elif  player1.rect.x > ball.rect.x - 43:
                        player1.rect.x -= 2
                else:
                    player1.rect.x == ball.rect.x + 8    
            if player1.rect.x >= Fieldstartx+boxWidth*2: player1.rect.x = Fieldstartx+boxWidth*2
            elif player1.rect.x <= Fieldstartx: player1.rect.x = Fieldstartx
            if player1.rect.y >= Fieldstarty + boxHeight*2: player1.rect.y = Fieldstarty + boxHeight*2
            elif player1.rect.y <= Fieldstarty: player1.rect.y = Fieldstarty 

        if redHasBall == True:
                    guess = random.uniform(2,15)
                    if timeR >= guess:
                        ball.shootRight()
                        ball.update()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        redHasBall = False
                        timeR = 0
    DefensiveP1R()
#Player2Red
    def OffensiveP2R():
        global redHasBall
        global timeR    
        if redHasBall == False:
            if ball.rect.x >= (Fieldstartx + boxWidth*2):
                if not player2.rect.y == ball.rect.y + 8:
                    if player2.rect.y < ball.rect.y + 8:
                        player2.rect.y += 2
                    elif  player2.rect.y > ball.rect.y - 43:
                        player2.rect.y -= 2
                else:
                    player2.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight*2) and ball.rect.y > (Fieldstarty + boxHeight):
                if not player2.rect.x == ball.rect.x + 8:
                    if player2.rect.x < ball.rect.x + 8:
                        player2.rect.x += 2
                    elif  player2.rect.x > ball.rect.x - 43:
                        player2.rect.x -= 2
                else:
                    player2.rect.x == ball.rect.x + 8    
            if player2.rect.x >= Fieldstartx+boxWidth*4-40: player2.rect.x = Fieldstartx+boxWidth*4-40
            elif player2.rect.x <= Fieldstartx + boxWidth*2: player2.rect.x = Fieldstartx + boxWidth*2
            if player2.rect.y >= Fieldstarty + boxHeight*2: player2.rect.y = Fieldstarty + boxHeight*2
            elif player2.rect.y <= Fieldstarty + boxHeight: player2.rect.y = Fieldstarty + boxHeight 

        if redHasBall == True:
                    guess = random.uniform(2,15)
                    if timeR >= guess:
                        accuracy = random.randint(1,3)
                        if accuracy > 1:
                            ball.shootRight()
                        else: ball.finishRight()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        redHasBall = False
                        timeR = 0
    def DefensiveP2R():
        global redHasBall
        global timeR    
        if redHasBall == False:
            if ball.rect.x >= (Fieldstartx + boxWidth*2):
                if not player2.rect.y == ball.rect.y + 8:
                    if player2.rect.y < ball.rect.y + 8:
                        player2.rect.y += 2
                    elif  player2.rect.y > ball.rect.y - 43:
                        player2.rect.y -= 2
                else:
                    player2.rect.y == ball.rect.y + 8
            if ball.rect.y >= (Fieldstarty):
                if not player2.rect.x == ball.rect.x + 8:
                    if player2.rect.x < ball.rect.x + 8:
                        player2.rect.x += 2
                    elif  player2.rect.x > ball.rect.x - 43:
                        player2.rect.x -= 2
                else:
                    player2.rect.x == ball.rect.x + 8    
            if player2.rect.x >= Fieldstartx+boxWidth*4-40: player2.rect.x = Fieldstartx+boxWidth*4-40
            elif player2.rect.x <= Fieldstartx + boxWidth*2: player2.rect.x = Fieldstartx + boxWidth*2
            if player2.rect.y >= Fieldstarty + boxHeight*2: player2.rect.y = Fieldstarty + boxHeight*2
            elif player2.rect.y <= Fieldstarty: player2.rect.y = Fieldstarty
        if redHasBall == True:
                    guess = random.uniform(2,15)
                    if timeR >= guess:
                        accuracy = random.randint(1,3)
                        if accuracy > 1:
                            ball.shootRight()
                        else: ball.finishRight()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        redHasBall = False
                        timeR = 0
    DefensiveP2R()
    #GoalKeeperBlue
    def GKB():
        global blueHasBall
        global timeB
        if blueHasBall == False:
            if ball.rect.x >= (Fieldstartx + boxWidth*3):
                if not player3.rect.y == ball.rect.y + 8:
                    if player3.rect.y < ball.rect.y + 8:
                        player3.rect.y += 2
                    elif  player3.rect.y > ball.rect.y - 43:
                        player3.rect.y -= 2
                else:
                    player3.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight*2):
                if not player3.rect.x == ball.rect.x + 8:
                    if player3.rect.x < ball.rect.x + 8:
                        player3.rect.x += 2
                    elif  player3.rect.x > ball.rect.x - 43:
                        player3.rect.x -= 2
                else:
                    player3.rect.x == ball.rect.x + 8    
            if player3.rect.x <= Fieldstartx + boxWidth*3: player3.rect.x = Fieldstartx + boxWidth*3
            elif player3.rect.x >= Fieldstartx+boxWidth*4: player3.rect.x = Fieldstartx+boxWidth*4
            if player3.rect.y >= 470: player3.rect.y = 470
            elif player3.rect.y <= Fieldstarty: player4.rect.y = Fieldstarty
        if blueHasBall == True:
                guess = random.uniform(2,15)
                if timeB >= guess:
                    ball.shootLeft()
                    ball.update()
                    effect = pygame.mixer.Sound('soundbounce.wav')
                    effect.play()
                    blueHasBall = False
                    timeB = 0
    GKB()
    #Player1Blue
    def OffensiveP1B():
        global blueHasBall
        global timeB
        if blueHasBall == False:
            if ball.rect.x <= (Fieldstartx + boxWidth*2):
                if not player4.rect.y == ball.rect.y + 8:
                    if player4.rect.y < ball.rect.y + 8:
                        player4.rect.y += 2
                    elif  player4.rect.y > ball.rect.y - 43:
                        player4.rect.y -= 2
                else:
                    player4.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight):
                if not player4.rect.x == ball.rect.x + 8:
                    if player4.rect.x < ball.rect.x + 8:
                        player4.rect.x += 2
                    elif  player4.rect.x > ball.rect.x - 43:
                        player4.rect.x -= 2
                else:
                    player4.rect.x == ball.rect.x + 8    
            if player4.rect.x <= Fieldstartx+40: player4.rect.x = Fieldstartx+40
            elif player4.rect.x >= Fieldstartx + boxWidth*2: player4.rect.x = Fieldstartx + boxWidth*2
            if player4.rect.y >= Fieldstarty + boxHeight: player4.rect.y = Fieldstarty + boxHeight
            elif player4.rect.y <= Fieldstarty: player4.rect.y = Fieldstarty
        if blueHasBall == True:
                guess = random.uniform(2,15)
                if timeB >= guess:
                        accuracy = random.randint(1,3)
                        if accuracy > 1:
                            ball.shootLeft()
                        else: ball.finishLeft()
                        ball.update()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        blueHasBall = False
                        timeB = 0
    def DefensiveP1B():
        global blueHasBall
        global timeB
        if blueHasBall == False:
            if ball.rect.x <= (Fieldstartx + boxWidth*3) and ball.rect.x >= (Fieldstartx + boxWidth*2):
                if not player4.rect.y == ball.rect.y + 8:
                    if player4.rect.y < ball.rect.y + 8:
                        player4.rect.y += 2
                    elif  player4.rect.y > ball.rect.y - 43:
                        player4.rect.y -= 2
                else:
                    player4.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight*2):
                if not player4.rect.x == ball.rect.x + 8:
                    if player4.rect.x < ball.rect.x + 8:
                        player4.rect.x += 2
                    elif  player4.rect.x > ball.rect.x - 43:
                        player4.rect.x -= 2
                else:
                    player4.rect.x == ball.rect.x + 8    
            if player4.rect.x <= Fieldstartx+boxWidth: player4.rect.x = Fieldstartx+boxWidth
            elif player4.rect.x >= Fieldstartx + boxWidth*2: player4.rect.x = Fieldstartx + boxWidth*2
            if player4.rect.y >= Fieldstarty + boxHeight: player4.rect.y = Fieldstarty + boxHeight
            elif player4.rect.y <= Fieldstarty: player4.rect.y = Fieldstarty
        if blueHasBall == True:
                guess = random.uniform(2,15)
                if timeB >= guess:
                        ball.shootLeft()
                        ball.update()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        blueHasBall = False
                        timeB = 0
    OffensiveP1B()   
#Player2Blue
    def OffensiveP2B():
        global blueHasBall
        global timeB
        if blueHasBall == False:
            if ball.rect.x <= (Fieldstartx + boxWidth*2):
                if not player5.rect.y == ball.rect.y + 8:
                    if player5.rect.y < ball.rect.y + 8:
                        player5.rect.y += 2
                    elif  player5.rect.y > ball.rect.y - 43:
                        player5.rect.y -= 2
                else:
                    player5.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight*2) and ball.rect.y > (Fieldstarty + boxHeight):
                if not player5.rect.x == ball.rect.x + 8:
                    if player5.rect.x < ball.rect.x + 8:
                        player5.rect.x += 2
                    elif  player5.rect.x > ball.rect.x - 43:
                        player5.rect.x -= 2
                else:
                    player5.rect.x == ball.rect.x + 8    
            if player5.rect.x <= Fieldstartx+40: player5.rect.x = Fieldstartx+40
            elif player5.rect.x >= Fieldstartx + boxWidth*2: player5.rect.x = Fieldstartx + boxWidth*2
            if player5.rect.y >= Fieldstarty + boxHeight*2: player5.rect.y = Fieldstarty + boxHeight*2
            elif player5.rect.y <= Fieldstarty + boxHeight: player5.rect.y = Fieldstarty + boxHeight
        if blueHasBall == True:
                guess = random.uniform(2,15)
                if timeB >= guess:
                        accuracy = random.randint(1,3)
                        if accuracy > 1:
                            ball.shootLeft()
                        else: ball.finishLeft()
                        ball.update()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        blueHasBall = False
                        timeB = 0
    def DefensiveP2B():
        global blueHasBall
        global timeB
        if blueHasBall == False:
            if ball.rect.x <= (Fieldstartx + boxWidth*2):
                if not player5.rect.y == ball.rect.y + 8:
                    if player5.rect.y < ball.rect.y + 8:
                        player5.rect.y += 2
                elif  player5.rect.y > ball.rect.y - 43:
                    player5.rect.y -= 2
                else:
                    player5.rect.y == ball.rect.y + 8
            if ball.rect.y <= (Fieldstarty + boxHeight*2):
                if not player5.rect.x == ball.rect.x + 8:
                    if player5.rect.x < ball.rect.x + 8:
                        player5.rect.x += 2
                elif  player5.rect.x > ball.rect.x - 43:
                    player5.rect.x -= 2
                else:
                    player5.rect.x == ball.rect.x + 8    
            if player5.rect.x <= Fieldstartx+40: player5.rect.x = Fieldstartx+40
            elif player5.rect.x >= Fieldstartx + boxWidth*2: player5.rect.x = Fieldstartx + boxWidth*2
            if player5.rect.y >= Fieldstarty + boxHeight*2: player5.rect.y = Fieldstarty + boxHeight*2
            elif player5.rect.y <= Fieldstarty: player5.rect.y = Fieldstarty
        if blueHasBall == True:
                guess = random.uniform(2,15)
                if timeB >= guess:
                        accuracy = random.randint(1,3)
                        if accuracy > 1:
                            ball.shootLeft()
                        else: ball.finishLeft()
                        ball.update()
                        effect = pygame.mixer.Sound('soundbounce.wav')
                        effect.play()
                        blueHasBall = False
                        timeB = 0
    OffensiveP2B()
   #for collisions
    if pygame.sprite.collide_mask(ball, goal1): #goal1 is the leftmost
        score2+=1 #if the left team scores right score increases
        ball.rect.x, ball.rect.y = 340, 235 #puts the ball in the middle of the field
        effect = pygame.mixer.Sound('soundscore.wav')
     
        effect.play()
        ball.pause() #method for pausing the speed of the ball
        for i in all_players_list:
            i.reset()
        ball.continuationLeft()
        sleep(3) 

    if  pygame.sprite.collide_mask(ball, goal2): #goal2 is the rightmost
        score1+=1 #if the right team scores left score increases
        ball.rect.x, ball.rect.y = 340, 235
        effect = pygame.mixer.Sound('soundscore.wav')
        for i in all_players_list:
            i.reset()
        effect.play()
        ball.pause() #method for pausing the speed of the ball

        ball.continuationRight()
        sleep(3) 

#collision with red team and ball passing
    for i in Team1: #Red Team
        if pygame.sprite.collide_rect(ball, i):
            redHasBall = True
            ball.rect.x, ball.rect.y = i.rect.x + 40, i.rect.y + 10
            ball.velocity = i.velocity

                    
#collision with blue team and ball passing
    for i in Team2: #Blue team 
        if pygame.sprite.collide_rect(ball, i):            
            blueHasBall = True
            ball.rect.x, ball.rect.y = i.rect.x - 20, i.rect.y + 10
            ball.velocity = i.velocity


    for i in all_players_list:
         for j in all_players_list:
            if (pygame.sprite.collide_rect(i,j) and i != j):
                 i.bounce()

    #if ball.rect.y>490:
       #ball.velocity[1] = -ball.velocity[1]
    #if ball.rect.y<0:
       #ball.velocity[1] = -ball.velocity[1]

#Field
    screen.fill(Green)
    pygame.draw.line(screen,White, [349, 0],[349, 500], 5)
    pygame.draw.rect(screen,Black, pygame.Rect(0,0,700,500),15)
    pygame.draw.rect(screen,White, pygame.Rect(15,15,670,470),5)
    #Fieldzones = {"A":[]}

    scr2text = scorefont.render(str(score2), 1, Black)
    scr1text = scorefont.render(str(score1), 1, Black)
          
    screen.blit(scr1text, (250,10))
    screen.blit(scr2text, (420,10))

    pygame.draw.circle(screen,White,[349,249],75,5)

    all_sprites_list.draw(screen)
    for i in all_players_list:
        i.update()
    ball.update()
    pygame.display.flip()
    screenUpdate.tick(50)
    print(timeR)
pygame.quit()        
