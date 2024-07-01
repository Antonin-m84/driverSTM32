"""
Consume data from queue and display in the grid gui
"""

import multiprocessing

from .plotColors import get_color

# Configuration
GRID_SIZE = 8
CELL_SIZE = 100
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 60


def consume_data(queue: multiprocessing.Queue):
    import pygame

    # Initialize Pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("8x8 Grid Visualization")
    font = pygame.font.SysFont(None, int(CELL_SIZE / 60 * 24))
    clock = pygame.time.Clock()

    def draw_grid(values):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                value = values[(GRID_SIZE-1-y) * GRID_SIZE + x]
                color = get_color(value)
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, color, rect)
                text = font.render(str(value), True, (255, 255, 255))
                window.blit(text, (x * CELL_SIZE + CELL_SIZE / 4, y * CELL_SIZE + CELL_SIZE / 4))

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