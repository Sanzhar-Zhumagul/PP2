import pygame, sys
from pygame.locals import *
import random
import os

# ------------------- ИСПРАВЛЕНИЕ ПУТЕЙ -------------------
# Эта строчка говорит Python искать файлы в той же папке, где лежит сам скрипт
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):
    return os.path.join(BASE_PATH, filename)

pygame.init()

# ------------------- НАСТРОЙКИ -------------------
FPS = 60
clock = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

ROAD_LEFT = 50
ROAD_RIGHT = 350

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (200, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game - Правильная версия")

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 35)

# ------------------- ОБЪЕКТ -------------------
class GameObject:
    def __init__(self, image_name, size, x, y, speed=0, controllable=False, is_coin=False):
        self.size = size
        self.is_coin = is_coin
        
        if self.is_coin:
            # Загружаем 3 вида монет через get_path
            self.coin_images = [
                pygame.transform.scale(pygame.image.load(get_path(f"coin{i}.png")).convert_alpha(), size)
                for i in [1, 2, 3]
            ]
            self.weight = 1
            self.image = self.coin_images[0]
        else:
            # Загружаем машину через get_path
            self.image = pygame.image.load(get_path(image_name)).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.controllable = controllable

    def update(self):
        if self.controllable:
            keys = pygame.key.get_pressed()
            if keys[K_LEFT] and self.rect.left > ROAD_LEFT:
                self.rect.x -= 5
            if keys[K_RIGHT] and self.rect.right < ROAD_RIGHT:
                self.rect.x += 5

        if self.speed > 0:
            self.rect.y += self.speed
            if self.rect.top > SCREEN_HEIGHT:
                self.reset()

    def reset(self):
        new_x = random.randint(ROAD_LEFT + self.rect.width // 2, 
                               ROAD_RIGHT - self.rect.width // 2)
        self.rect.center = (new_x, -100)
        
        if self.is_coin:
            coin_type = random.randint(0, 2)
            self.image = self.coin_images[coin_type]
            self.weight = [1, 3, 5][coin_type]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# ------------------- ДОРОГА -------------------
def draw_road(surface, offset):
    surface.fill(GRAY)
    pygame.draw.line(surface, WHITE, (ROAD_LEFT, 0), (ROAD_LEFT, SCREEN_HEIGHT), 5)
    pygame.draw.line(surface, WHITE, (ROAD_RIGHT, 0), (ROAD_RIGHT, SCREEN_HEIGHT), 5)
    
    for y in range(-40, SCREEN_HEIGHT, 40):
        pygame.draw.line(surface, YELLOW, (SCREEN_WIDTH//2, y + offset), (SCREEN_WIDTH//2, y + 20 + offset), 5)

# ------------------- ФУНКЦИИ ИГРЫ -------------------
def reset_game():
    global player, enemy, coin, coin_count, road_offset, game_over
    player = GameObject("player.png", (60, 120), 200, 520, controllable=True)
    enemy = GameObject("enemy.png", (58, 116), 200, -150, speed=5)
    coin = GameObject("coin1.png", (30, 30), 200, -50, speed=5, is_coin=True)
    coin_count = 0
    road_offset = 0
    game_over = False

reset_game()

# ------------------- ОСНОВНОЙ ЦИКЛ -------------------
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if game_over and event.type == KEYDOWN:
            if event.key == K_f:
                reset_game()

    if not game_over:
        player.update()
        enemy.update()
        coin.update()
        road_offset = (road_offset + 5) % 40

        if player.rect.colliderect(coin.rect):
            prev_score = coin_count
            coin_count += coin.weight
            if (coin_count // 10) > (prev_score // 10):
                enemy.speed += 1.0
            coin.reset()
            while coin.rect.colliderect(enemy.rect):
                coin.reset()

        if player.rect.colliderect(enemy.rect):
            game_over = True

    # ОТРИСОВКА
    draw_road(screen, road_offset)
    coin.draw(screen)
    player.draw(screen)
    enemy.draw(screen)

    # UI
    s_txt = font.render(f"Score: {coin_count}", True, WHITE)
    v_txt = font.render(f"Speed: {int(enemy.speed)}", True, WHITE)
    screen.blit(s_txt, (10, 10))
    screen.blit(v_txt, (10, 35))

    if game_over:
        # Эффект затемнения
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(160)
        overlay.fill(BLACK)
        screen.blit(overlay, (0,0))
        
        over_msg = big_font.render("GAME OVER", True, RED)
        screen.blit(over_msg, (SCREEN_WIDTH//2 - over_msg.get_width()//2, 200))
        
        btn_rect = pygame.Rect(SCREEN_WIDTH//2 - 110, 300, 220, 50)
        pygame.draw.rect(screen, WHITE, btn_rect, border_radius=10)
        btn_txt = font.render("Press F to Restart", True, BLACK)
        screen.blit(btn_txt, (btn_rect.centerx - btn_txt.get_width()//2, btn_rect.centery - btn_txt.get_height()//2))

    pygame.display.update()
    clock.tick(FPS)