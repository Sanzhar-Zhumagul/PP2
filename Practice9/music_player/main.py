import pygame
import sys
from player import MusicPlayer
# Настройки окна
WIDTH, HEIGHT = 600, 400
FPS = 30
# Цвета
WHITE = (245, 245, 245)
BLACK = (30, 30, 30)
BLUE = (0, 114, 225)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()
    # Шрифты
    title_font = pygame.font.SysFont('Arial', 28, bold=True)
    info_font = pygame.font.SysFont('Arial', 20)
    timer_font = pygame.font.SysFont('Consolas', 18)
    # Инициализация плеера
    player = MusicPlayer(music_dir='music')
    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_SPACE:
                    player.pause()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next()
                elif event.key == pygame.K_b:
                    player.prev()
                elif event.key == pygame.K_q:
                    running = False

        pos_ms = player.get_pos_ms()
        seconds = int((pos_ms / 1000) % 60)
        minutes = int((pos_ms / (1000 * 60)) % 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        
        # Заголовок
        title_surf = title_font.render("Music Controller", True, BLACK)
        screen.blit(title_surf, (WIDTH//2 - title_surf.get_width()//2, 40))

        # Название трека
        current_track = player.get_current_track_name()
        track_surf = info_font.render(current_track, True, DARK_GRAY)
        screen.blit(track_surf, (WIDTH//2 - track_surf.get_width()//2, 110))

        # Статус плеера
        status = "PLAYING" if player.is_playing else ("PAUSED" if player.is_paused else "STOPPED")
        status_color = BLUE if player.is_playing else DARK_GRAY
        status_surf = info_font.render(status, True, status_color)
        screen.blit(status_surf, (WIDTH//2 - status_surf.get_width()//2, 150))

        # Полоса прогресса
        bar_x, bar_y, bar_w, bar_h = 50, 210, 500, 12
        pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_w, bar_h), border_radius=5)
        
        # Визуальный индикатор 
        progress_width = (pos_ms // 100) % bar_w if player.is_playing else 0
        if player.is_playing or player.is_paused:
             actual_progress = min((pos_ms // 500), bar_w) 
             pygame.draw.rect(screen, BLUE, (bar_x, bar_y, actual_progress, bar_h), border_radius=5)

        # Таймер
        time_surf = timer_font.render(time_str, True, BLACK)
        screen.blit(time_surf, (bar_x + bar_w - time_surf.get_width(), bar_y + 20))

        # Блок управления
        hint_y = 320
        controls = [
            ("P", "Play"), ("SPACE", "Pause"), ("S", "Stop"), 
            ("N", "Next"), ("B", "Back"), ("Q", "Quit")
        ]
        ctrl_x_start = 60
        for key, action in controls:
            k_surf = timer_font.render(key, True, BLUE)
            a_surf = small_font = pygame.font.SysFont('Arial', 14).render(action, True, DARK_GRAY)
            screen.blit(k_surf, (ctrl_x_start, hint_y))
            screen.blit(a_surf, (ctrl_x_start, hint_y + 20))
            ctrl_x_start += 90
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()