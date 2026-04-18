import pygame
import sys
from ball import Ball
def main():
    pygame.init()
    # Настройки экрана
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Red Ball")
    # Цвета
    WHITE = (255, 255, 255)
    # Создание объекта мяча
    ball = Ball(WIDTH, HEIGHT)
    clock = pygame.time.Clock()
    while True:
        # 1. Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Обработка одиночных нажатий клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move(0, -ball.step)
                elif event.key == pygame.K_DOWN:
                    ball.move(0, ball.step)
                elif event.key == pygame.K_LEFT:
                    ball.move(-ball.step, 0)
                elif event.key == pygame.K_RIGHT:
                    ball.move(ball.step, 0)
        # 2. Отрисовка
        screen.fill(WHITE)
        ball.draw(screen)
        pygame.display.flip()
        # 3. Контроль частоты кадров
        clock.tick(60)

if __name__ == "__main__":
    main()