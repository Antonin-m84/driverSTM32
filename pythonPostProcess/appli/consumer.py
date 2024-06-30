"""
Consume data from queue and display in the grid gui
"""

import multiprocessing

from appli.plotColors import get_color

# Configuration
GRID_SIZE = 8
CELL_SIZE = 60
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 60
VALUE_RANGE = (0, 3000)
COLOR_RANGE = [(0, 255, 0), (0, 0, 255), (128, 0, 128)]  # Light green to blue to dark purple


def consume_data(queue: multiprocessing.Queue):
    import pygame

    # Initialize Pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("8x8 Grid Visualization")
    font = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()

    def draw_grid(values):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = values[i * GRID_SIZE + j]
                color = get_color(value)
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, color, rect)
                text = font.render(str(value), True, (255, 255, 255))
                window.blit(text, (j * CELL_SIZE + CELL_SIZE / 4, i * CELL_SIZE + CELL_SIZE / 4))

    def update(queue, current_values):
        try:
            while True:
                # if not queue.empty():
                #     data = queue.get()
                #     print("Received data:", data)

                values = queue.get_nowait()
                current_values[:] = values
        except Exception as e:
            pass

    current_values = [0] * 64

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # process.terminate()
                pygame.quit()
                exit()

        update(queue, current_values)

        window.fill((0, 0, 0))
        draw_grid(current_values)
        pygame.display.flip()

        clock.tick(FPS)