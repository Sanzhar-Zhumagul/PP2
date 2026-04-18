import pygame
import datetime
import os

pygame.init()
WIDTH, HEIGHT = 650, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()

# 📌 фиксируем путь к папке проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 📌 загрузка изображений через абсолютный путь
bg = pygame.image.load(os.path.join(BASE_DIR, 'images/mickeyclock.png')).convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

hand_min = pygame.image.load(os.path.join(BASE_DIR, 'images/hand1.png')).convert_alpha()
hand_sec = pygame.image.load(os.path.join(BASE_DIR, 'images/hand2.png')).convert_alpha()

center = (WIDTH // 2, HEIGHT // 2)

MIN_CORRECTION = 147  # твоя калибровка

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()

    angle_sec = -now.second * 6 - 90
    angle_min = -(now.minute + now.second / 60) * 6 - 90 + MIN_CORRECTION

    screen.blit(bg, (0, 0))

    rotated_sec = pygame.transform.rotate(hand_sec, angle_sec)
    screen.blit(rotated_sec, rotated_sec.get_rect(center=center))

    rotated_min = pygame.transform.rotate(hand_min, angle_min)
    screen.blit(rotated_min, rotated_min.get_rect(center=center))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()