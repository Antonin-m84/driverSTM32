import time
import multiprocessing
from typing import List
import pygame
import os

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 80

def replay_data(queue: multiprocessing.Queue):
    def get_lines():
        with open('session_log.csv', 'r') as file:
            return file.readlines()

    lines = get_lines()
    total_lines = len(lines)
    current_index = 0
    start_epoch = float(lines[0].split(";")[0])
    end_epoch = float(lines[total_lines-1].split(";")[0])

    has_moved = True

    # Initialize Pygame for keyboard control
    x = 10
    y = 10
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Replay Control")
    font = pygame.font.SysFont(None, 32)
    small_font = pygame.font.SysFont(None, 18)
    clock = pygame.time.Clock()

    def display_epoch(epoch_time):
        screen.fill((0, 0, 0))
        text = small_font.render(f'Epoch: {epoch_time}', True, (255, 255, 255))
        screen.blit(text, (10, 10))
        pygame.display.flip()

    def draw_timeline(start_epoch, end_epoch, current_epoch):
        relative_end = end_epoch - start_epoch
        relative_pos = current_epoch - start_epoch
        # text = small_font.render(f'{0:<8.2f} - {relative_pos:<8.2f} - {relative_end:<8.2f}', True, (255, 255, 255))
        text = small_font.render(f'{0} - {current_index:<8} - {total_lines-1:<8}', True, (255, 255, 255))
        screen.blit(text, (10, 60))

        progress_width = WINDOW_WIDTH - 10
        pygame.draw.rect(screen, (57, 57, 57), pygame.Rect(5, 30, progress_width, 20))
        pygame.draw.rect(screen, (37, 177, 77), pygame.Rect(5, 30, progress_width/relative_end*relative_pos, 20))

        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:  # Appuis long sur touche
                if event.key == pygame.K_LEFT:
                    current_index = min(current_index + 1, total_lines - 1)
                    has_moved = True
                elif event.key == pygame.K_LEFT:
                    current_index = max(current_index - 1, 0)
                    has_moved = True
            elif event.type == pygame.KEYUP:  # Relâcher touche
                if event.key == pygame.K_n:
                    current_index = min(current_index + 1, total_lines - 1)
                    has_moved = True
                elif event.key == pygame.K_p:
                    current_index = max(current_index - 1, 0)
                    has_moved = True

        # Handle fast forward and rewind
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            current_index = min(current_index + 1, total_lines - 1)
            has_moved = True
        elif keys[pygame.K_LEFT]:
            current_index = max(current_index - 1, 0)
            has_moved = True

        if has_moved:
            line = lines[current_index]

            epoch_time, *values = line.split(";")
            values = list(map(int, values))

            print(current_index)
            print(values)
            queue.put(values)
            has_moved = False

            display_epoch(epoch_time)
            draw_timeline(start_epoch, end_epoch, float(epoch_time))


            clock.tick(200 if keys[pygame.K_SPACE] else 20)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    replay_data(queue)