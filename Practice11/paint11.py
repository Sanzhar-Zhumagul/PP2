import pygame
import math # Нужен для расчета координат треугольников

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    canvas = pygame.Surface((800, 600))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'line' 
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'black': (0, 0, 0)
    }
    current_color_key = 'blue'
    
    drawing = False
    points = [] 
    start_pos = None 

    while True:
        screen.fill((0, 0, 0))
        screen.blit(canvas, (0, 0))
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return
                
                # Выбор инструментов
                if event.key == pygame.K_1: mode = 'line'
                if event.key == pygame.K_2: mode = 'rect'
                if event.key == pygame.K_3: mode = 'circle'
                if event.key == pygame.K_4: mode = 'eraser'
                # Новые инструменты:
                if event.key == pygame.K_5: mode = 'square'
                if event.key == pygame.K_6: mode = 'right_tr'
                if event.key == pygame.K_7: mode = 'eq_tr'
                if event.key == pygame.K_8: mode = 'rhombus'
                
                if event.key == pygame.K_r: current_color_key = 'red'
                elif event.key == pygame.K_g: current_color_key = 'green'
                elif event.key == pygame.K_b: current_color_key = 'blue'
                elif event.key == pygame.K_y: current_color_key = 'yellow'

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                if mode in ['line', 'eraser']:
                    points = [event.pos]

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    # Список "статичных" фигур, которые рисуются по двум точкам
                    if mode not in ['line', 'eraser']:
                        draw_shape(canvas, start_pos, event.pos, mode, colors[current_color_key])
                    drawing = False
                    points = []

            if event.type == pygame.MOUSEWHEEL:
                radius = max(1, min(100, radius + event.y * 2))

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if mode in ['line', 'eraser']:
                        new_point = event.pos
                        points.append(new_point)
                        if len(points) > 1:
                            c = colors['black'] if mode == 'eraser' else colors[current_color_key]
                            draw_smooth_line(canvas, points[-2], points[-1], radius, c)
        
        # Отрисовка превью (динамический просмотр фигуры при зажатой мыши)
        if drawing and mode not in ['line', 'eraser']:
            draw_shape(screen, start_pos, mouse_pos, mode, colors[current_color_key])

        pygame.display.set_caption(f"Инструмент: {mode} | Цвет: {current_color_key} | Радиус: {radius}")
        pygame.display.flip()
        clock.tick(120)

def draw_smooth_line(surface, start, end, radius, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), radius)

def draw_shape(surface, start, end, mode, color):
    x1, y1 = start
    x2, y2 = end
    
    # Вспомогательные переменные для определения границ рисования
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if mode == 'rect':
        # Обычный прямоугольник
        pygame.draw.rect(surface, color, (left, top, width, height), 2)
        
    elif mode == 'circle':
        # Окружность: центр в точке нажатия, радиус — расстояние до курсора
        rad = int(((x1 - x2)**2 + (y1 - y2)**2)**0.5)
        pygame.draw.circle(surface, color, start, rad, 2)

    elif mode == 'square':
        # Квадрат: берем бОльшую сторону, чтобы фигура была симметричной
        side = max(width, height)
        # Учитываем направление движения мыши (влево/вправо и вверх/вниз)
        new_x = x1 if x2 > x1 else x1 - side
        new_y = y1 if y2 > y1 else y1 - side
        pygame.draw.rect(surface, color, (new_x, new_y, side, side), 2)

    elif mode == 'right_tr':
        # Прямоугольный треугольник: прямой угол в точке (x1, y2)
        points = [(x1, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(surface, color, points, 2)

    elif mode == 'eq_tr':
        # Равносторонний треугольник:
        # Мы берем ширину области и вычисляем высоту по формуле h = a * sqrt(3) / 2
        # Это гарантирует, что треугольник будет "правильным"
        side = width
        h = int(side * (3**0.5) / 2)
        
        # Центрируем треугольник относительно начальной точки x1
        # Направление отрисовки (вверх/вниз) зависит от движения мыши по оси Y
        direction = 1 if y2 > y1 else -1
        points = [
            (x1, y1),                       # Вершина
            (x1 - side // 2, y1 + h * direction), # Левый угол
            (x1 + side // 2, y1 + h * direction)  # Правый угол
        ]
        pygame.draw.polygon(surface, color, points, 2)

    elif mode == 'rhombus':
        # Ромб: точки пересечения диагоналей по осям X и Y
        # Центр ромба — в точке первого нажатия
        points = [
            (x1, y1 - height), # Верх
            (x1 + width, y1),  # Право
            (x1, y1 + height), # Низ
            (x1 - width, y1)   # Лево
        ]
        pygame.draw.polygon(surface, color, points, 2)

if __name__ == "__main__":
    main()