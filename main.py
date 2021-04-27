import pygame
pygame.font.init()
pygame.init()
win = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Pong")
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
R = 255
G = 255
B = 255
cursorX= 155
cursorY= 167
rainbow = 0
myfont = pygame.font.SysFont('Comic Sans MS', 60)
tutorialFont=pygame.font.SysFont('arial', 14)
nameFont=pygame.font.SysFont('arial bold', 25)
x = 15
y = 100
y2 = 100
x2 = 475
ballx = 250
bally = 150
width = 15
height = 80
vel = 6
ballvel = 7
ballvel2 = 6
Moveup = 0
Movedown = 0
ballspeed = 7
gamespeed = 50
P1_Score = 0
P2_Score = 0
Text1_Y = 220
Text2_Y = 255
tutorial = 1
loop = 1
loop2 = 1
Letter1 = 1
Letter2 = 1
P1=""
P2=""
letterPOS=1
run = True
while run:
  if tutorial == 1:
    while loop2 == 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        keys = pygame.key.get_pressed()
        win.fill((0, 0, 0))
        Name1=nameFont.render("Player 1, what is your name?", False, (255, 255, 255))
        win.blit(Name1,(130, 100))
        keyboard=nameFont.render(" A  B  C  D  E  F  G  H  I", False, (255, 255, 255))
        win.blit(keyboard,(150, 150))
        keyboard2=nameFont.render(" J  K   L  M  N O P  Q  R", False, (255, 255, 255))
        win.blit(keyboard2,(150, 180))
        keyboard3=nameFont.render(" S  T  U  V  W  X  Y  Z  .", False, (255, 255, 255))
        win.blit(keyboard3,(150, 210))
        pygame.draw.rect(win, (R, G, B), (cursorX, cursorY, 15, 3))
        if keys[pygame.K_d]:
          cursorX+=21
          pygame.time.delay(400)
          Letter1+=1
        if keys[pygame.K_a]:
          if cursorX >= 155:
            cursorX-=21
            pygame.time.delay(400)
            Letter1-=1
        if keys[pygame.K_w]:
          if cursorY>=168:
            cursorY-=30
            Letter2+=1
            pygame.time.delay(400)
        if keys[pygame.K_s]:
          if cursorY<=267:
            cursorY+=30
            Letter2+=1
            pygame.time.delay(400)
        if keys[pygame.K_SPACE]:
          if Letter2==1:
            if Letter1==1:
              P1=P1+"A"
              pygame.time.delay(500)
            if Letter1==2:
              P1=P1+"B"
              pygame.time.delay(500)
            if Letter1==3:
              P1=P1+"C"
              pygame.time.delay(500)
            if Letter1==4:
              P1=P1+"D"
              pygame.time.delay(500)
            if Letter1==5:
              P1=P1+"E"
              pygame.time.delay(500)
            if Letter1==6:
              P1=P1+"F"
              pygame.time.delay(500)
            if Letter1==7:
              P1=P1+"G"
              pygame.time.delay(500)
            if Letter1==8:
              P1=P1+"H"
              pygame.time.delay(500)
            if Letter1==9:
              P1=P1+"I"
              pygame.time.delay(500)
          if Letter2==2:
            if Letter1==1:
              P1=P1+"J"
              pygame.time.delay(500)
            if Letter1==2:
              P1=P1+"K"
              pygame.time.delay(500)
            if Letter1==3:
              P1=P1+"L"
              pygame.time.delay(500)
            if Letter1==4:
              P1=P1+"M"
              pygame.time.delay(500)
            if Letter1==5:
              P1=P1+"N"
              pygame.time.delay(500)
            if Letter1==6:
              P1=P1+"O"
              pygame.time.delay(500)
            if Letter1==7:
              P1=P1+"P"
              pygame.time.delay(500)
            if Letter1==8:
              P1=P1+"Q"
              pygame.time.delay(500)
            if Letter1==9:
              P1=P1+"R"
              pygame.time.delay(500)
          if Letter2==3:
            if Letter1==1:
              P1=P1+"S"
              pygame.time.delay(500)
            if Letter1==2:
              P1=P1+"T"
              pygame.time.delay(500)
            if Letter1==3:
              P1=P1+"U"
              pygame.time.delay(500)
            if Letter1==4:
              P1=P1+"V"
              pygame.time.delay(500)
            if Letter1==5:
              P1=P1+"W"
              pygame.time.delay(500)
            if Letter1==6:
              P1=P1+"X"
              pygame.time.delay(500)
            if Letter1==7:
              P1=P1+"Y"
              pygame.time.delay(500)
            if Letter1==8:
              P1=P1+"Z"
              pygame.time.delay(500)
            if Letter1==9:
              P1=P1+"."
              pygame.time.delay(500)
        if keys[pygame.K_LSHIFT]:
          loop2=2  
          cursorX=155
          cursorY=167
          Letter1=1
          Letter2=1
        pygame.display.update() 
    win.fill((0, 0, 0))
    pygame.display.update()
    PTW=int(input("How many points are we playing to? "))
    Text3 = tutorialFont.render("P1 Don't let the ball touch the green", False, (150, 150, 255))
    win.blit(Text3,(x,y-30))
    Text4 = tutorialFont.render("P2 Get past the paddle and touch the green", False, (80, 255, 80))
    win.blit(Text4,(ballx-150,bally-30))
    Title = myfont.render("REVERSE PONG", False, (255, 255, 255))
    win.blit(Title,(100,0))
    P1 = nameFont.render(P1, False, (255, 255, 255))
    win.blit(P1, (x, y+90))
    P2 = nameFont.render(P2, False, (255, 255, 255))
    win.blit(P2, (ballx-(150), bally+30))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.display.update()
  pygame.time.delay(gamespeed)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  #Player 1 (Paddle) Controls: W and S
  if keys[pygame.K_w]:
    if y >= 10:
      y -= vel
  if keys[pygame.K_s]:
    if y <= 219:
      y += vel
  #Player 2 (Ball) Controls: Up and Down
  if Moveup >= 1:
    bally += ballvel2
    Moveup = Moveup-1
  elif keys[pygame.K_UP]:
    if bally >= 10:
      bally -= ballvel2
    else:
      Moveup = 10
  if bally >= 39:
    if bally <= 265:
      y2 = bally - 40
  if Movedown >= 1:
    bally -= ballvel2
    Movedown = Movedown-1
  elif keys[pygame.K_DOWN]:
    if bally <= 289:
      bally += ballvel2 
    else:
      Movedown = 10
  #Hit Detection
  if ballx <= 50 and ballx >= 43:
    if y <= bally and y + 80 >= bally:
      if ballspeed <= -7:
        P1_Score = P1_Score+1
        ballspeed = -ballspeed
        ballvel = ballvel + .1
  if ballx >= 475:
    ballspeed = -ballspeed
    ballvel = ballvel + .05
  if ballx <= 10:
    P2_Score = P2_Score+1
    ballspeed = -ballspeed
    ballvel = ballvel + .05
  if ballspeed >= 0:
    ballx += ballvel
  if ballspeed <= 0:
    ballx -= ballvel
  win.fill((0, 0, 0))
  if P1_Score >= 10:
    Text1_Y = 195
  P1_Sco = str(P1_Score)
  P2_Sco = str(P2_Score)
  #Draw Screen
  textsurface = myfont.render(P1_Sco, False, (255, 255, 255))
  win.blit(textsurface,(Text1_Y,0))
  textsurface2 = myfont.render(P2_Sco, False, (255, 255, 255))
  win.blit(textsurface2,(Text2_Y,0))
  tutorial = 2
  pygame.draw.rect(win, white, (x2, y2, width, height))
  pygame.draw.rect(win, white, (x, y, width, height))
  pygame.draw.rect(win, white, (249.5, 0, 1, 300))
  pygame.draw.rect(win, green,  (0, 0, 3, 300))
  pygame.draw.circle(win, white, (250, 150), 40)
  pygame.draw.circle(win, black, (250, 150), 39)
  pygame.draw.circle(win, (R, G, B), (ballx, bally), 10)
  pygame.display.update()
  #Winscreen
  if P2_Score>=PTW:
    P2_Win = myfont.render("PLAYER 2 WINS", False, (255, 255, 0))
    win.blit(P2_Win,(100,200))
    pygame.display.update()
    pygame.time.delay(5000)
    run = False
    pygame.quit()
  if P1_Score>=PTW:
    P1_Win = myfont.render("PLAYER 1 WINS", False, (255, 255, 0))
    win.blit(P1_Win,(100,200))
    pygame.display.update()
    pygame.time.delay(5000)
    run = False
    pygame.quit()
pygame.quit()