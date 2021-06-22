#So, aparently, my game allows for Online Play with join links?! Pretty sick, I'd reccomend trying it. Just fork my repl and send the join link to your friends!
import pygame
pygame.font.init()
pygame.init()
win = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Reverse Pong")
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
R = 255
G = 255
B = 255
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
vel = 7
ballvel = 5
ballvel2 = 6
Moveup = 0
Movedown = 0
ballspeed = 7
gamespeed = 30
P1_Score = 0
P2_Score = 0
Text1_Y = 220
Text2_Y = 255
tutorial = 1
P1=""
P2=""
run = True
while run:
  if tutorial == 1:
    win.fill((0, 0, 0))
    pygame.display.update()
    #User Input
    P1 =(input("What is your name, Player 1? "))
    P2 =(input("What is your name, Player 2? "))
    PTW=(input("How many points are we playing to? "))
    if PTW==(""):
      PTW=10
    PTW=int(PTW)
    #Tutorial
    Text3 = tutorialFont.render("P1 Don't let the ball touch the green", False, (150, 150, 255))
    win.blit(Text3,(x,y-30))
    Text4 = tutorialFont.render("P2 Get past the paddle and touch the green", False, (80, 255, 80))
    win.blit(Text4,(ballx-150,bally-30))
    Title = myfont.render("REVERSE PONG", False, (255, 255, 255))
    win.blit(Title,(100,0))
    P1 = nameFont.render(P1, False, (255, 255, 255))
    win.blit(P1, (50, 150))
    P2 = nameFont.render(P2, False, (255, 255, 255))
    win.blit(P2, (300, 150))
    VS = nameFont.render("VS", False, (255, 255, 255))
    win.blit(VS, (240, 150))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.display.update()
  pygame.time.delay(gamespeed)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  keys = pygame.key.get_pressed()
  #Player 1 (Paddle) Controls: W and S
  if keys[pygame.K_w]:
    if y >= 3:
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
  if ballx <= 50 and ballx >= 42:
    if y-5 <= bally and y + 80 >= bally:
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