import random
import time
import math
import pygame
pygame.font.init()
import sys
mode = input('would you like to play multi player or against the ai?(mp or ai)')
vel = 5
ball_radius = 10
ball_height = ball_radius
ball_width = ball_radius
ball_speed = input('what speed do you want the ball (slow, medium, fast)? ')
helping = False
if 'o' in ball_speed.lower():
  ball_down = 1
  ball_right = -3
elif 'm' in ball_speed.lower():
  ball_down = 3
  ball_right = -5
else:
  ball_down = 6
  ball_right = -10
vel = 5
clock = pygame.time.Clock()
pong_height = 100
pong_width = 3
user_x = 10
ai_score = 0
user_score = 0
font = pygame.font.Font(None, 72)
def help():
  help = [ball_x, ball_y, ball_down, ball_right]
  line = [ball_x, ball_y]
  lines = []
  while help[0] > 10:
    if help[0] > display_width - 13:
      break
    help[0] += help[3]
    help[1] += help[2]
    if help[1] - (ball_height / 2) <= 0 or help[1] + (ball_height / 2) >= display_height:
      if help[2] > 0:
        help[2] = -help[2]
      else:
        help[2] = abs(help[2])
      line.append(help[0])
      line.append(help[1])
      lines.append(line)
      line = [help[0], help[1]]
    if help[0] >= ((display_width - 10) - ball_width) and help[1] >= help[1] and help[1] <= help[1] + pong_height:
      help[3] = -help[3]
      line.append(help[0])
      line.append(help[1])
      lines.append(line)
      line = [help[0], help[1]]
  line.append(help[0])
  line.append(help[1])
  lines.append(line)
  line = []
  return lines
def find_ball():
  target = [ball_x, ball_y, ball_down, ball_right]
  while target[0] < display_width - 13:
    target[0] += target[3]
    target[1] += target[2]
    if target[1] - (ball_height / 2) <= 0 or target[1] + (ball_height / 2) >= display_height:
      if target[2] > 0:
        target[2] = -target[2]
      else:
        target[2] = abs(target[2])
    if target[0] < (14 + (ball_radius / 2) + pong_width):
      target[3] = abs(target[3])
  return target
if 'mp' in mode.lower():
  print('To exit, push e')
  time.sleep(2)
  screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  display_width, display_height = pygame.display.get_surface().get_size()
  ball_x = math.floor(display_width / 2)
  ball_y = math.floor(display_height / 2)
  user_y = (display_height / 2) - (pong_height / 2)
  ai_x = (display_width - 10) - pong_width
  ai_y = user_y
  pygame.display.set_caption('P O N G')
  while True:
    if ball_x < 0:
      ai_score += 1
      ball_x = math.floor(display_width / 2)
    if ball_x > display_width:
      user_score += 1
      ball_x = math.floor(display_width / 2)
    ball_x += ball_right
    ball_y += ball_down
    if ball_y - (ball_height / 2) <= 0 or ball_y + (ball_height / 2) >= display_height:
      if ball_down > 0:
        ball_down = -ball_down
      else:
        ball_down = abs(ball_down)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and user_y >= 0:
      user_y -= vel
    if key[pygame.K_s] and user_y < display_height - pong_height:
      user_y += vel
    if key[pygame.K_DOWN] and ai_y <= (display_height - pong_height):
      ai_y += vel
    if key[pygame.K_UP] and ai_y >= 0:
      ai_y -= vel
    if key[pygame.K_e]:
      pygame.quit()
    #  if ball_x - 5 < 14 and user_y <= ball_y and user_y - pong_height >= ball_y:
    if ball_x < (14 + (ball_radius / 2) + pong_width) and ball_y >= user_y and ball_y <= user_y + pong_height:
      if ball_right > 0:
        ball_right = -ball_right
      else:
        ball_right = abs(ball_right)
      if random.randint(0, 1):
        if ball_down > 0:
          ball_down = -ball_down
        else:
          ball_down = abs(ball_down)
    if ball_x >= ((display_width - 10) - ball_width) and ball_y >= ai_y and ball_y <= ai_y + pong_height:
      if ball_right > 0:
        ball_right = -ball_right
      else:
        ball_right = abs(ball_right)
      if random.randint(0, 1):
        if ball_down > 0:
          ball_down = -ball_down
        else:
          ball_down = abs(ball_down)
    ai_point_x = display_width - 25
    ai_point_y = 25
    user_point_x = 25
    user_point_y = 25
    ai_row = 0
    user_row = 0
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)
    pygame.draw.rect(screen, (255, 255, 255), (user_x, user_y, pong_width, pong_height))
    pygame.draw.rect(screen, (255, 255, 255), (ai_x, ai_y, pong_width, pong_height))
    for i in range(ai_score):
      pygame.draw.circle(screen, (255, 255, 255), (ai_point_x, ai_point_y), 5)
      ai_point_x -= 25
      ai_row += 1
      if ai_row % 5 == 0:
        ai_point_y += 25
        ai_point_x = display_width - 25
    for i in range(user_score):
      pygame.draw.circle(screen, (255, 255, 255), (user_point_x, user_point_y), 5)
      user_point_x += 25
      user_row += 1
      if user_row % 5 == 0:
        user_point_x = 25
        user_point_y += 25
    pygame.display.update()
else:
  mode = input('would you like to play on easy, medium, hard, or expert? ')
  if 'y' in mode.lower():
    ai_vel = vel / 4
  if 'm' in mode.lower():
    ai_vel = vel / 2
  if 'h' in mode.lower():
    ai_vel = vel
  if 't' in mode.lower():
    ai_vel = vel / 5
  print('For help, press "h". to deactivate help, hold "u".\nPush e to exit.')
  time.sleep(3)
  screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
  display_width, display_height = pygame.display.get_surface().get_size()
  pygame.display.set_caption('P O N G')
  ball_x = math.floor(display_width / 2)
  ball_y = math.floor(display_height / 2)
  user_y = (display_height / 2) - (pong_height / 2)
  ai_x = (display_width - 10) - pong_width
  ai_y = user_y
  while True:
    target = find_ball()
    while target[1] > display_height:
      target = find_ball()
    if target[1] - 50 > ai_y and ai_y <= (display_height - pong_height):
      ai_y += ai_vel
    if target[1] - 50 < ai_y and ai_y >= 5:
      ai_y -= ai_vel
    if ball_x < 0:
      ai_score += 1
      ball_x = math.floor(display_width / 2)
    if ball_x > display_width:
      user_score += 1
      ball_x = math.floor(display_width / 2)
    ball_x += ball_right
    ball_y += ball_down
    if ball_y - (ball_height / 2) <= 0 or ball_y + (ball_height / 2) >= display_height:
      if ball_down > 0:
        ball_down = -ball_down
      else:
        ball_down = abs(ball_down)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN] and user_y <= (display_height - pong_height):
      user_y += vel
    if key[pygame.K_UP] and user_y >= 0:
      user_y -= vel
    if key[pygame.K_h]:
      helping = True
    if key[pygame.K_u]:
      helping = False
    if key[pygame.K_e]:
      pygame.quit()
    #  if ball_x - 5 < 14 and user_y <= ball_y and user_y - pong_height >= ball_y:
    if ball_x < (14 + (ball_radius / 2) + pong_width) and ball_y >= user_y and ball_y <= user_y + pong_height:
      if ball_right > 0:
        ball_right = -ball_right
      else:
        ball_right = abs(ball_right)
    if ball_x >= ((display_width - 10) - ball_width) and ball_y >= ai_y and ball_y <= ai_y + pong_height:
      if ball_right > 0:
        ball_right = -ball_right
      else:
        ball_right = abs(ball_right)
    ai_point_x = display_width - 25
    ai_point_y = 25
    user_point_x = 25
    user_point_y = 25
    ai_row = 0
    user_row = 0
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)
    pygame.draw.rect(screen, (255, 255, 255), (user_x, user_y, pong_width, pong_height))
    pygame.draw.rect(screen, (255, 255, 255), (ai_x, ai_y, pong_width, pong_height))
    for i in range(ai_score):
      pygame.draw.circle(screen, (255, 255, 255), (ai_point_x, ai_point_y), 5)
      ai_point_x -= 25
      ai_row += 1
      if ai_row % 5 == 0:
        ai_point_y += 25
        ai_point_x = display_width - 25
    for i in range(user_score):
      pygame.draw.circle(screen, (255, 255, 255), (user_point_x, user_point_y), 5)
      user_point_x += 25
      user_row += 1
      if user_row % 5 == 0:
        user_point_x = 25
        user_point_y += 25
    if helping:
      lines = help()
      for i in range(len(lines)):
        pygame.draw.line(screen, (0, 0, 255), [lines[i][0], lines[i][1]], [lines[i][2], lines[i][3]], 3)
    pygame.display.update()
