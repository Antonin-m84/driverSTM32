"""
Consomme les data depuis la queue et les affichent dans la grille du GUI
"""

import multiprocessing
from .plotColors import get_color
import time


# Configuration
GRID_SIZE = 8
CELL_SIZE = 100
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 60


def consume_data(queue: multiprocessing.Queue, do_log: bool = True):
    import pygame

    # Initialize Pygame : crée le GUI et la grille
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("GUI 8x8 Data visualisation")
    font = pygame.font.SysFont(None, int(CELL_SIZE / 60 * 24))
    clock = pygame.time.Clock()

    # Joint les data dans la grille
    def draw_grid(values):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                    try:
                        # ici y inversé pour que le sol soit en bas de la grille
                        # value = values[y * GRID_SIZE + x]
                        value = values[(GRID_SIZE-1-y) * GRID_SIZE + x]
                        color = get_color(value) # Fait référence au plotColors.py
                        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(window, color, rect)
                        text = font.render(str(value), True, (255, 255, 255))
                        window.blit(text, (x * CELL_SIZE + CELL_SIZE / 4, y * CELL_SIZE + CELL_SIZE / 4))
                    except Exception as e:
                        print(e)

    # Met à jour les data
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

    if do_log:
        output = open('session_log.csv', 'wb+', buffering=4096)
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # process.terminate()
                    pygame.quit()
                    exit()

            update(queue, current_values)
            # log values to text file
            if do_log:
                output.write((str(time.time() * 1000) + ";" + ';'.join(map(str, current_values)) + '\r\n').encode('utf-8'))

            window.fill((0, 0, 0))
            draw_grid(current_values)
            pygame.display.flip()

            clock.tick(FPS)
    finally:
        output.close()