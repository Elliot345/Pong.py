import random
import math
import pygame
pygame.font.init()
import sys
mode = input('would you like to play multi player or against the ai?(mp or ai)')
vel = 5
display_width = 1200
display_height = 600
ball_x = math.floor(display_width / 2)
ball_y = math.floor(display_height / 2)
pygame.display.set_caption('P O N G')
ball_radius = 10
ball_height = ball_radius
ball_width = ball_radius
ball_speed = input('what speed do you want the ball (slow, medium, fast)? ')
if 'o' in ball_speed.lower():
  ball_down = 1
  ball_right = -2
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
user_y = (display_height / 2) - (pong_height / 2)
ai_x = (display_width - 10) - pong_width
ai_y = user_y
ai_score = 0
user_score = 0
font = pygame.font.Font(None, 72)
def find_ball():
  target = [ball_x, ball_y, ball_down, ball_right]
  while target[0] < 1200 - 10:
    target[0] += target[3]
    target[1] += target[2]
    if target[1] - (ball_height / 2) <= 0 or target[1] + (ball_height / 2) >= display_height:
      if target[2] > 0:
        target[2] = -target[2]
      else:
        target[2] = abs(target[2])
    if target[0] - (ball_width / 2) <= 10:
      target[3] = abs(target[3])
  return target
if 'mp' in mode.lower():
  screen = pygame.display.set_mode((display_width, display_height))
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
    ai_vel = vel / 10
  if 'm' in mode.lower():
    ai_vel = vel / 8
  if 'h' in mode.lower():
    ai_vel = vel / 6
  if 't' in mode.lower():
    ai_vel = vel / 5
  screen = pygame.display.set_mode((display_width, display_height))
  while True:
    target = find_ball()
    while target[1] > 600:
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
