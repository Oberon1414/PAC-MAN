import pygame
import math


pygame.init()
WIDTH = 700  #Задание размеров окна
HEIGHT = 750
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60        #Не нуждается в объяснении
font = pygame.font.SysFont('Times New Roman', 20)     #Шрифт
# 0 = пустое место, 1 = обычная точка, 2 = большая точка, 3 = вертикальная стена,
# 4 = горизонтальная стена, 5 = угол право-вверх, 6 = угол лево-вверх, 7 = лево-вниз, 8 = право-вниз
# 9 = ворота для призраков
board = [
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
[5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
[3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
[3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
[3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
         ]
pi = math.pi

player_stages = []  #Составляем список из картинок стадий пакмэна и стартовые координаты
for i in range(1, 5):
    player_stages.append(pygame.transform.scale(
        pygame.image.load(f'player{i}.png'), [25, 25]))
spooky_img = pygame.transform.scale(
        pygame.image.load(f'powerup.png'), [25, 25])
dead_img = pygame.transform.scale(
        pygame.image.load(f'dead.png'), [25, 25])
player_x = 335
player_y = 500
player_speed = 1
command = 'right'
direction = 'right'
frame_counter = 0
flicker = False
start_time = 180
moving = False
powerup_active = False
power_time = 0
invincible = False
invinc_time = 0
score = 0
lives = 3
game_won = False
victory_sfx_played = False
game_over = False
game_over_sfx_played = False
waka_waka_sfx = pygame.mixer.Sound('Waka Waka.mp3')
sound_timer = 0
life_lost_sfx = pygame.mixer.Sound('Life lost.mp3')
powerup_sfx = pygame.mixer.Sound('Powerup.mp3')


class Ghost:
    def __init__(self, x, y, target, direction, color, speed=player_speed, is_dead=False, is_revived=False):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(
            pygame.image.load(f'{color}.png'), [25, 25])
        self.target = target
        self.direction = direction
        self.color = color
        self.is_dead = is_dead
        self.is_revived = is_revived
        self.speed = speed
        self.turns, self.in_box = self.check_position()

    def draw(self):
        if (not self.is_dead and not powerup_active) or self.is_revived:
            screen.blit(self.image, [self.x, self.y])
        elif powerup_active and not self.is_dead and not self.is_revived:
            screen.blit(spooky_img, [self.x, self.y])
        elif self.is_dead:
            screen.blit(dead_img, [self.x, self.y])

    def check_position(self):
        self.turns = [False, False, False, False]
        tile_height = (HEIGHT - 50) // 32
        tile_width = WIDTH // 30
        fudge = 10
        center_x = self.x + 13
        center_y = self.y + 13
        if 1 < center_x // tile_width < 29:
            if board[(center_y - fudge) // tile_height][center_x // tile_width] == 9:
                self.turns[2] = True
            if board[center_y // tile_height][(center_x - fudge) // tile_width] < 3 \
                    or (board[center_y // tile_height][(center_x - fudge) // tile_width] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[1] = True
            if board[center_y // tile_height][(center_x + fudge) // tile_width] < 3 \
                    or (board[center_y // tile_height][(center_x + fudge) // tile_width] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[0] = True
            if board[(center_y + fudge) // tile_height][center_x // tile_width] < 3 \
                    or (board[(center_y + fudge) // tile_height][center_x // tile_width] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[3] = True
            if board[(center_y - fudge) // tile_height][center_x // tile_width] < 3 \
                    or (board[(center_y - fudge) // tile_height][center_x // tile_width] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[2] = True

            if self.direction == 'up' or self.direction == 'down':
                if (tile_width - 7)//2 + 1 <= center_x % tile_width <= (tile_width + 7)//2:
                    if board[(center_y + fudge) // tile_height][center_x // tile_width] < 3 \
                            or (board[(center_y + fudge) // tile_height][center_x // tile_width] == 9 and (
                            self.in_box or self.is_dead)):
                        self.turns[3] = True
                    if board[(center_y - fudge) // tile_height][center_x // tile_width] < 3 \
                            or (board[(center_y - fudge) // tile_height][center_x // tile_width] == 9 and (
                            self.in_box or self.is_dead)):
                        self.turns[2] = True
                if (tile_height - 7)//2 + 1 <= center_y % tile_height <= (tile_height + 7)//2:
                    if board[center_y // tile_height][(center_x - tile_width) // tile_width] < 3 \
                            or (board[center_y // tile_height][(center_x - tile_width) // tile_width] == 9 and (
                            self.in_box or self.is_dead)):
                        self.turns[1] = True
                    if board[center_y // tile_height][(center_x + tile_width) // tile_width] < 3 \
                            or (board[center_y // tile_height][(center_x + tile_width) // tile_width] == 9 and (
                            self.in_box or self.is_dead)):
                        self.turns[0] = True

            if self.direction == 'right' or self.direction == 'left':
                if (tile_width - 3) // 2 + 1 <= center_x % tile_width <= (tile_width + 3) // 2:
                    if board[(center_y + fudge) // tile_height][center_x // tile_width] < 3 \
                            or (board[(center_y + fudge) // tile_height][center_x // tile_width] == 9 and (
                            self.in_box or self.is_dead)):
                        self.turns[3] = True
                    if board[(center_y - fudge) // tile_height][center_x // tile_width] < 3 \
                            or (board[(center_y - fudge) // tile_height][center_x // tile_width] == 9 and (
                            self.in_box or self.is_dead)):
                        self.turns[2] = True
                if (tile_height - 3)//2 + 1 <= center_y % tile_height <= (tile_height + 3)//2:
                    if board[center_y // tile_height][(center_x - fudge) // tile_width] < 3 \
                            or (board[center_y // tile_height][(center_x - fudge) // tile_width] == 9 and (
                            self.in_box or self.is_dead)):
                        self.turns[1] = True
                    if board[center_y // tile_height][(center_x + fudge) // tile_width] < 3 \
                            or (board[center_y // tile_height][(center_x + fudge) // tile_width] == 9 and (
                            self.in_box or self.is_dead)):
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 266 <= self.x <= 401 and 280 <= self.y <= 346:
            self.in_box = True
        else:
            self.in_box = False
        if self.in_box:
            self.is_dead = False
            self.is_revived = True
            self.speed = player_speed
        if not self.in_box and not powerup_active and self.is_revived:
            self.is_revived = False
        return self.turns, self.in_box

    def update_target(self):
        if powerup_active and not self.is_dead and not self.is_revived:
            if player_x < 350:
                target_x = 700
            else:
                target_x = 0
            if player_y < 350:
                target_y = 700
            else:
                target_y = 0
            if self.color == 'blue':
                target_y = player_y
            elif self.color == 'pink':
                target_x = player_x
            elif self.color == 'orange':
                target_x = 330
                target_y = 315
        elif self.in_box:
            target_x = 330
            target_y = 250
        elif self.is_dead:
            target_x = 330
            target_y = 315
        else:
            target_x = player_x
            target_y = player_y
        self.target = [target_x, target_y]

    def move_Inky(self):
        #Инки поворачивает вверх и вниз когда угодно, но вправо или влево только при столкновении
        if self.direction == 'right':
            if self.target[0] > self.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
            elif self.turns[0]:
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                if self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                else:
                    self.x += self.speed
        elif self.direction == 'left':
            if self.target[1] > self.y and self.turns[3]:
                self.direction = 'down'
            elif self.target[0] < self.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
            elif self.turns[1]:
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                if self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                else:
                    self.x -= self.speed
        elif self.direction == 'up':
            if self.target[1] < self.y and self.turns[2]:
                self.direction = 'up'
                self.y -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
            elif self.turns[2]:
                self.y -= self.speed
        elif self.direction == 'down':
            if self.target[1] > self.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
            elif self.turns[3]:
                self.y += self.speed
        return self.x, self.y, self.direction

    def move_Pinky(self):
        #Пинки поворачивает налево и направо в любой момент, но вверх и вниз только, когда вынужден
        if self.direction == 'right':
            if self.target[0] > self.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
            elif self.turns[0]:
                self.x += self.speed
        elif self.direction == 'left':
            if self.target[1] > self.y and self.turns[3]:
                self.direction = 'down'
            elif self.target[0] < self.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
            elif self.turns[1]:
                self.x -= self.speed
        elif self.direction == 'up':
            if self.target[0] < self.x and self.turns[1]:
                self.direction = 'left'
                self.x -= self.speed
            elif self.target[1] < self.y and self.turns[2]:
                self.direction = 'up'
                self.y -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
            elif self.turns[2]:
                if self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                else:
                    self.y -= self.speed
        elif self.direction == 'down':
            if self.target[1] > self.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
            elif self.turns[3]:
                if self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                else:
                    self.y += self.speed
        return self.x, self.y, self.direction

    def move_Blinky(self):
        #Блинки поворачивает только когда вынужден
        if self.direction == 'right':
            if self.target[0] > self.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
            elif self.turns[0]:
                self.x += self.speed
        elif self.direction == 'left':
            if self.target[0] < self.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
            elif self.turns[1]:
                self.x -= self.speed
        elif self.direction == 'up':
            if self.target[1] < self.y and self.turns[2]:
                self.direction = 'up'
                self.y -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
            elif self.turns[2]:
                self.y -= self.speed
        elif self.direction == 'down':
            if self.target[1] > self.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x and self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.target[0] < self.x and self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
            elif self.turns[3]:
                self.y += self.speed
        return self.x, self.y, self.direction

    def move_Clyde(self):
        #Клайд поворачивает всегда, когда это выгодно
        if self.direction == 'right':   #Если сейчас идёт вправо...
            if self.target[0] > self.x and self.turns[0]:   #можно продолжить идти направо и это выгодно
                self.x += self.speed
            elif not self.turns[0]: #справа тупик, нужно повернуть
                if self.target[1] < self.y and self.turns[2]:  #наверх можно и выгодно
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.target[1] > self.y and self.turns[3]:  #вниз можно и выгодно
                    self.direction = 'down'
                    self.y += self.speed
                elif self.target[0] < self.x and self.turns[1]:  #влево можно и выгодно
                    self.direction = 'left'  #поскольку текущее движение - вправо, то поворот налево имеет наименьший приоритет
                    self.x -= self.speed
                elif self.turns[2]:     #тупик, но все выгодные пути недоступны, так что поворот в пределах того же приоритета
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
            elif self.turns[0]:     #Направо можно, но цель не правее
                if self.target[1] < self.y and self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                else:  #поворот обратно без тупика не происходит, т.к. выгодно в случае туннеля
                    self.x += self.speed
        elif self.direction == 'left':   #Если сейчас идёт влево...
            if self.target[1] < self.y and self.turns[2]: #немного меняем порядок приоритетов, чтобы уменьшить вероятность застрять в петле туда-сюда
                self.direction = 'up'  #Если можно вверх и выгодно, повернуть ввверх
                self.y -= self.speed
            elif self.target[0] < self.x and self.turns[1]:   #можно продолжить идти налево и это выгодно
                self.x -= self.speed
            elif not self.turns[1]: #слева тупик, нужно повернуть
                if self.target[1] > self.y and self.turns[3]:  #вниз можно и выгодно (вверх уже рассмотрели выше)
                    self.direction = 'down'
                    self.y += self.speed
                elif self.target[0] > self.x and self.turns[0]:  #вправо можно и выгодно
                    self.direction = 'right'  #поскольку текущее движение - влево, то поворот направо имеет наименьший приоритет
                    self.x += self.speed
                elif self.turns[2]:  #тупик, но все выгодные пути недоступны, так что поворот в пределах того же приоритета
                    self.direction = 'up'
                    self.y -= self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                elif self.turns[0]:
                    self.direction = 'right'
                    self.x += self.speed
            elif self.turns[1]:     #Налево можно, но цель не левее
                if self.target[1] > self.y and self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
                else:  #поворот обратно без тупика не происходит, т.к. выгодно в случае туннеля
                    self.x -= self.speed
        elif self.direction == 'up':   #Если сейчас идёт вверх...
            if self.target[0] > self.x and self.turns[0]: #немного меняем порядок приоритетов, чтобы уменьшить вероятность застрять в петле туда-сюда
                self.direction = 'right'  #Если можно вправо и выгодно, повернуть вправо
                self.x += self.speed
            elif self.target[1] < self.y and self.turns[2]:   #можно продолжить идти наверх и это выгодно
                self.y -= self.speed
            elif not self.turns[2]: #сверху тупик, нужно повернуть
                if self.target[0] < self.x and self.turns[1]:  #влево можно и выгодно (вправо уже рассмотрели выше)
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.target[1] > self.y and self.turns[3]:  #вниз можно и выгодно
                    self.direction = 'down'     #поскольку текущее движение - вверх, то поворот вниз имеет наименьший приоритет
                    self.y += self.speed
                elif self.turns[0]:  #тупик, но все выгодные пути недоступны, так что поворот в пределах того же приоритета
                    self.direction = 'right'
                    self.x += self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[3]:
                    self.direction = 'down'
                    self.y += self.speed
            elif self.turns[2]:     #Наверх можно, но цель не выше
                if self.target[0] < self.x and self.turns[1]:  # влево можно и выгодно (вправо уже рассмотрели выше)
                    self.direction = 'left'
                    self.x -= self.speed
                else:  #поворот обратно без тупика не происходит, т.к. выгодно в случае туннеля
                    self.y -= self.speed
        elif self.direction == 'down':   #Если сейчас идёт вниз...
            if self.target[0] > self.x and self.turns[0]: #немного меняем порядок приоритетов, чтобы уменьшить вероятность застрять в петле туда-сюда
                self.direction = 'right'  #Если можно вправо и выгодно, повернуть вправо
                self.x += self.speed
            elif self.target[1] > self.y and self.turns[3]:   #можно продолжить идти вниз и это выгодно
                self.y += self.speed
            elif not self.turns[3]: #снизу тупик, нужно повернуть
                if self.target[0] < self.x and self.turns[1]:  #влево можно и выгодно (вправо уже рассмотрели выше)
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.target[1] < self.y and self.turns[2]:  #вверх можно и выгодно
                    self.direction = 'up'     #поскольку текущее движение - вниз, то поворот вверх имеет наименьший приоритет
                    self.y -= self.speed
                elif self.turns[0]:  #тупик, но все выгодные пути недоступны, так что поворот в пределах того же приоритета
                    self.direction = 'right'
                    self.x += self.speed
                elif self.turns[1]:
                    self.direction = 'left'
                    self.x -= self.speed
                elif self.turns[2]:
                    self.direction = 'up'
                    self.y -= self.speed
            elif self.turns[3]:     #Наверх можно, но цель не выше
                if self.target[0] < self.x and self.turns[1]:  # влево можно и выгодно (вправо уже рассмотрели выше)
                    self.direction = 'left'
                    self.x -= self.speed
                else:  #поворот обратно без тупика не происходит, т.к. выгодно в случае туннеля
                    self.y += self.speed
        return self.x, self.y, self.direction


Inky = Ghost(276, 294, [player_x, player_y], 'right', 'blue')
Pinky = Ghost(276, 336, [player_x, player_y], 'right', 'pink')
Blinky = Ghost(46, 42, [player_x, player_y], 'right', 'red')
Clyde = Ghost(391, 315, [player_x, player_y], 'left', 'orange')


def draw_board(board):       #Рисуем поле
    color = "Blue"  # Цвет стен
    tile_height = (HEIGHT - 50) // 32
    tile_width = WIDTH // 30
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                pygame.draw.circle(screen, "White", [(j + 0.5) * tile_width, (i+0.5) * tile_height], 3)
            elif board[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, "White", [(j + 0.5) * tile_width, (i+0.5) * tile_height], 6)
            elif board[i][j] == 3:
                pygame.draw.line(screen, color, [(j + 0.5) * tile_width, i * tile_height],
                                 [(j + 0.5) * tile_width, (i + 1) * tile_height], 3)
            elif board[i][j] == 4:
                pygame.draw.line(screen, color, [j * tile_width, (i+0.5) * tile_height],
                                 [(j + 1) * tile_width, (i + 0.5) * tile_height], 3)
            elif board[i][j] == 5:
                pygame.draw.arc(screen, color, [(j-0.4) * tile_width - 2, (i+0.5)*tile_height,
                                                tile_width, tile_height], 0, pi/2, 3)
            elif board[i][j] == 6:
                pygame.draw.arc(screen, color, [(j+0.5) * tile_width, (i+0.5)*tile_height,
                                                tile_width, tile_height], pi/2, pi, 3)
            elif board[i][j] == 7:
                pygame.draw.arc(screen, color, [(j+0.5) * tile_width, (i-0.4)*tile_height,
                                                tile_width, tile_height], pi, 3*pi/2, 2)
            elif board[i][j] == 8:
                pygame.draw.arc(screen, color, [(j-0.4) * tile_width - 2, (i-0.4)*tile_height,
                                                tile_width, tile_height], 3*pi/2, 2*pi, 2)
            elif board[i][j] == 9:
                pygame.draw.line(screen, 'White', [j * tile_width, (i+0.5) * tile_height],
                                 [(j + 1) * tile_width, (i + 0.5) * tile_height], 3)


def draw_ui(score, powerup_active, power_time, invincible, invinc_time):
    score_text = font.render(f'Score: {score}', True, 'White')
    screen.blit(score_text, [10, 715])
    screen.blit(font.render('Lives:', True, 'White'), [425, 715])
    if powerup_active:
        pygame.draw.circle(screen, 'White', [140, 730], 16)
        pygame.draw.circle(screen, 'Blue', [140, 730], 15)
        power_countdown_text = font.render(f'{power_time // 60 + 1}', True, 'White')
        if power_time // 60 + 1 == 10:
            screen.blit(power_countdown_text, [129, 719])
        else:
            screen.blit(power_countdown_text, [135, 719])
    if invincible:
        pygame.draw.circle(screen, 'White', [200, 730], 16)
        pygame.draw.circle(screen, 'Red', [200, 730], 15)
        invinc_countdown_text = font.render(f'{invinc_time // 60 + 1}', True, 'White')
        screen.blit(invinc_countdown_text, [195, 719])
    for i in range(lives):
        screen.blit(pygame.transform.scale(player_stages[0], [16, 16]), [500 + i*40, 720])
    if game_over or game_won:
        pygame.draw.rect(screen, 'White', [50, 200, 600, 300], 0, 10)
        pygame.draw.rect(screen, 'Dark gray', [70, 220, 560, 260], 0, 10)
        if game_over:
            screen.blit(font.render('Game over. Press spacebar to restart', True, 'Red'), [210, 330])
        if game_won:
            screen.blit(font.render('Victory! Press spacebar to restart', True, 'Green'), [220, 330])


def draw_player():      #Рисуем пакмэна
    if direction == "right":
        screen.blit(player_stages[frame_counter // 5], [player_x, player_y])
    elif direction == "left":
        screen.blit(pygame.transform.flip(player_stages[frame_counter // 5], True, False), [player_x, player_y])
    elif direction == "up":
        screen.blit(pygame.transform.rotate(player_stages[frame_counter // 5], 90), [player_x, player_y])
    elif direction == "down":
        screen.blit(pygame.transform.rotate(player_stages[frame_counter // 5], -90), [player_x, player_y])


def check_position(center_x, center_y):
    turns = [False, False, False, False]
    tile_height = (HEIGHT - 50) // 32
    tile_width = WIDTH // 30
    fudge = 10      #погрешность из-за неровности кругов и чтобы не останавливаться за полклетки от стены
    if 1 < (center_x // tile_width) < 29:
        # Можно ли идти в обратную сторону от текущего направления
        if direction == "right":
            if board[center_y//tile_height][(center_x - fudge) // tile_width] < 3:
                turns[1] = True
        if direction == "left":
            if board[center_y//tile_height][(center_x + fudge) // tile_width] < 3:
                turns[0] = True
        if direction == "up":
            if board[(center_y + fudge)//tile_height][center_x//tile_width] < 3:
                turns[3] = True
        if direction == "down":
            if board[(center_y - fudge) // tile_height][center_x // tile_width] < 3:
                turns[2] = True

        #Можно ли поворачивать, идя вверх или вниз (так, чтобы не поломать систему клеток и не идти сквозь стены)
        if direction == "up" or direction == 'down':
            if (tile_width - 7)//2 + 1 <= center_x % tile_width <= (tile_width + 7)//2:  #по центру ли клетки по x
                if board[(center_y + fudge)//tile_height][center_x//tile_width] < 3:  #можно вниз
                    turns[3] = True
                if board[(center_y - fudge)//tile_height][center_x//tile_width] < 3:  #можно вверх
                    turns[2] = True
            if (tile_height - 7)//2 + 1 <= center_y % tile_height <= (tile_height + 7)//2:  #по центру ли по y
                if board[center_y//tile_height][(center_x - tile_width)//tile_width] < 3:   # проверяем наличие туннеля влево
                    turns[1] = True
                if board[center_y // tile_height][(center_x + tile_width)//tile_width] < 3: # проверяем наличие туннеля вправо
                    turns[0] = True

            # Можно ли поворачивать, идя вправо или влево (так, чтобы не поломать систему клеток и не идти сквозь стены)
        if direction == "right" or direction == 'left':
            if (tile_width - 7) // 2 + 1 <= center_x % tile_width <= (
                    tile_width + 7) // 2:  # по центру ли клетки по x
                if board[(center_y + tile_height) // tile_height][center_x // tile_width] < 3:  # проверяем наличие туннеля вниз
                    turns[3] = True
                if board[(center_y - tile_height) // tile_height][center_x // tile_width] < 3:  # проверяем наличие туннеля вверх
                    turns[2] = True
            if (tile_height - 7) // 2 + 1 <= center_y % tile_height <= (tile_height + 7) // 2:  # по центру ли по y
                if board[center_y // tile_height][(center_x - fudge) // tile_width] < 3:  # можно влево
                    turns[1] = True
                if board[center_y // tile_height][(center_x + fudge) // tile_width] < 3:  # можно вправо
                    turns[0] = True

    else:
        #Единственный способ зайти на границу карты по оси x - это через туннель. А в туннеле можно идти только влево и вправо
        turns[0] = True
        turns[1] = True

    return turns


def move_player(player_x, player_y):
    if direction == 'right' and valid_turns[0]:
        player_x += player_speed
    elif direction == "left" and valid_turns[1]:
        player_x -= player_speed
    elif direction == 'up' and valid_turns[2]:
        player_y -= player_speed
    elif direction == 'down' and valid_turns[3]:
        player_y += player_speed
    return player_x, player_y


def distance(player_x, player_y, ghost):
    return ((player_x - (ghost.x + 13))**2 + (player_y - (ghost.y+13))**2)**0.5


def check_collisions(center_x, center_y, score, powerup_taken, power_time, lives, invincible, invic_time):
    tile_height = (HEIGHT - 50) // 32
    tile_width = WIDTH // 30
    if 1 < (center_x // tile_width) < 29:
        if board[center_y//tile_height][center_x//tile_width] == 1:
            board[center_y // tile_height][center_x // tile_width] = 0
            score += 10
        elif board[center_y//tile_height][center_x//tile_width] == 2:
            board[center_y // tile_height][center_x // tile_width] = 0
            score += 50
            powerup_taken = True
            powerup_sfx.play()
            power_time = 600

    if distance(center_x, center_y, Inky) <= 25:
        if powerup_active and not Inky.is_dead:
            Inky.is_dead = True
            Inky.is_revived = False
            Inky.speed = 2*player_speed
            score += 100
        elif not powerup_active and not invincible and not Inky.is_dead and not game_won and not game_over:
            lives -= 1
            invincible = True
            invic_time = 180
            if lives != 0:
                life_lost_sfx.play()
    if distance(center_x, center_y, Pinky) <= 25:
        if powerup_active and not Pinky.is_dead:
            Pinky.is_dead = True
            Pinky.is_revived = False
            Pinky.speed = 2 * player_speed
            score += 100
        elif not powerup_active and not invincible and not Pinky.is_dead and not game_won and not game_over:
            lives -= 1
            invincible = True
            invic_time = 180
            if lives != 0:
                life_lost_sfx.play()
    if distance(center_x, center_y, Blinky) <= 25:
        if powerup_active and not Blinky.is_dead:
            Blinky.is_dead = True
            Blinky.is_revived = False
            Blinky.speed = player_speed*2
            score += 100
        elif not powerup_active and not invincible and not Blinky.is_dead and not game_won and not game_over:
            lives -= 1
            invincible = True
            invic_time = 180
            if lives != 0:
                life_lost_sfx.play()
    if distance(center_x, center_y, Clyde) <= 25:
        if powerup_active and not Clyde.is_dead:
            Clyde.is_dead = True
            Clyde.is_revived = False
            Clyde.speed = player_speed*2
            score += 100
        elif not powerup_active and not invincible and not Clyde.is_dead and not game_won and not game_over:
            lives -= 1
            invincible = True
            invic_time = 180
            if lives != 0:
                life_lost_sfx.play()
    return score, powerup_taken, power_time, lives, invincible, invic_time


def draw_all_ghosts():
    Inky.update_target()
    Inky.turns, Inky.in_box = Inky.check_position()
    Inky.draw()
    Pinky.update_target()
    Pinky.turns, Pinky.in_box = Pinky.check_position()
    Pinky.draw()
    Blinky.turns, Blinky.in_box = Blinky.check_position()
    Blinky.update_target()
    Blinky.draw()
    Clyde.update_target()
    Clyde.turns, Clyde.in_box = Clyde.check_position()
    Clyde.draw()


def move_all_ghosts():
    if Inky.is_dead or Inky.in_box:
        Inky.x, Inky.y, Inky.direction = Inky.move_Clyde()
    elif ((power_time % 2 == 0 and invinc_time == 0) or Inky.is_revived) and not game_won and not game_over:
        Inky.x, Inky.y, Inky.direction = Inky.move_Inky()
    if Pinky.is_dead or Pinky.in_box:
        Pinky.x, Pinky.y, Pinky.direction = Pinky.move_Clyde()
    elif ((power_time % 2 == 0 and invinc_time == 0) or Pinky.is_revived) and not game_won and not game_over:
        Pinky.x, Pinky.y, Pinky.direction = Pinky.move_Pinky()
    if Blinky.is_dead or Blinky.in_box:
        Blinky.x, Blinky.y, Blinky.direction = Blinky.move_Clyde()
    elif ((power_time % 2 == 0 and invinc_time == 0) or Blinky.is_revived) and not game_won and not game_over:
        Blinky.x, Blinky.y, Blinky.direction = Blinky.move_Blinky()
    if Clyde.is_dead or Clyde.is_revived:
        Clyde.x, Clyde.y, Clyde.direction = Clyde.move_Clyde()
    elif power_time % 2 == 0 and invinc_time == 0 and not game_won and not game_over:
        Clyde.x, Clyde.y, Clyde.direction = Clyde.move_Clyde()


run = True
waka_waka_sfx.set_volume(0.3)
waka_waka_sfx.play()
while run:
    timer.tick(fps)
    sound_timer += 1
    if frame_counter < 19:     #счётчик кадров для анимации
        frame_counter += 1
        if frame_counter > 5:
            flicker = False  #Мерцание больших точек
    else:
        frame_counter = 0
        flicker = True     #Поставить на False, чтобы не мерцали
    if powerup_active and power_time > 0:
        power_time -= 1
    elif powerup_active and power_time <= 0:
        powerup_active = False
        power_time = 0
    if invincible and invinc_time > 0:
        invinc_time -= 1
    elif invincible and invinc_time <= 0:
        invincible = False
        invinc_time = 0
    if sound_timer >= 180 and not game_won and not game_over:
        waka_waka_sfx.stop()
        waka_waka_sfx.play()
        sound_timer = 0

    screen.fill("Black")
    draw_board(board)
    draw_player()
    draw_all_ghosts()
    draw_ui(score, powerup_active, power_time, invincible, invinc_time)

    if start_time > 0 or game_over or game_won:
        moving = False
        if start_time > 0:
            countdown_text = font.render(f'{start_time//60 + 1}', True, 'White')
            screen.blit(countdown_text, [340, 315])
            start_time -= 1
    else:
        moving = True

    valid_turns = check_position(player_x + 13, player_y + 13) #поиск доступных поворотов
    Blinky.turns, Blinky.in_box = Blinky.check_position()
    if moving:
        player_x, player_y = move_player(player_x, player_y)  #перемещение
        move_all_ghosts()

    score, powerup_active, power_time, lives, invincible, invinc_time = check_collisions(player_x + 13, player_y + 13,
                        score, powerup_active, power_time, lives, invincible, invinc_time)

    #исполнитель кнопок
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #Выход из игры
            run = False
        elif event.type == pygame.KEYDOWN:  #Ввод команды. Даже если сейчас поворот недоступен, он запомнит
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                command = 'right'
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                command = 'left'
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                command = 'up'
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                command = 'down'
            elif (game_won or game_over) and event.key == pygame.K_SPACE:
                board = [
                    [6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
                    [3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
                    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
                    [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
                    [3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
                    [3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
                    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
                    [3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
                    [3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
                    [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
                    [3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
                    [3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
                    [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
                    [8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
                    [4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
                    [5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
                    [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
                    [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
                    [3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
                    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
                    [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
                    [3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
                    [3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
                    [3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
                    [3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
                    [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
                    [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
                    [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
                    [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
                    [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
                    [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
                ]
                player_x = 335
                player_y = 500
                player_speed = 1
                command = 'right'
                direction = 'right'
                frame_counter = 0
                flicker = False
                start_time = 180
                moving = False
                powerup_active = False
                power_time = 0
                invincible = False
                invinc_time = 0
                score = 0
                lives = 3
                sound_timer = 0
                game_won = False
                victory_sfx_played = False
                game_over = False
                game_over_sfx_played = False
                Inky = Ghost(276, 294, [player_x, player_y], 'right', 'blue')
                Pinky = Ghost(276, 336, [player_x, player_y], 'right', 'pink')
                Blinky = Ghost(46, 42, [player_x, player_y], 'right', 'red')
                Clyde = Ghost(391, 315, [player_x, player_y], 'left', 'orange')

    #Проверка возможности исполнения команды
    if command == 'right' and valid_turns[0]:
        direction = 'right'
    elif command == 'left' and valid_turns[1]:
        direction = 'left'
    elif command == 'up' and valid_turns[2]:
        direction = 'up'
    elif command == 'down' and valid_turns[3]:
        direction = 'down'

    if player_x > 710:
        player_x = -5
    elif player_x < -10:
        player_x = 705
    if Inky.x > 710:
        Inky.x = -5
    elif Inky.x < -10:
        Inky.x = 705
    if Pinky.x > 710:
        Pinky.x = -5
    elif Pinky.x < -10:
        Pinky.x = 705
    if Blinky.x > 710:
        Blinky.x = -5
    elif Blinky.x < -10:
        Blinky.x = 705
    if Clyde.x > 710:
        Clyde.x = -5
    elif Clyde.x < -10:
        Clyde.x = 705

    if lives <= 0:
        game_over = True
        waka_waka_sfx.stop()
        game_over_sfx = pygame.mixer.Sound('Game over.mp3')
        if not game_over_sfx_played:
            game_over_sfx.play()
            game_over_sfx_played = True

    game_won = True
    for i in board:
        if 1 in i or 2 in i:
            game_won = False
    if game_won and not game_over_sfx_played:
        waka_waka_sfx.stop()
        game_won_sfx = pygame.mixer.Sound('Game won.mp3')
        game_won_sfx.play()
        game_over_sfx_played = True

    pygame.display.flip()   #Смена кадра
pygame.quit()
