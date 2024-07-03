import multiprocessing
import time

import serial
import multiprocessing
from typing import List


def produce_data(queue: multiprocessing.Queue):
    while True:
        # Generate random values for the grid
        d = round(time.time() * 100) % 5000
        d2 = round(time.time() * 10) % 5000

        values = [d if _ %2 else d2 for _ in range(64)]
        queue.put(values)
        # Simulate high frequency by waiting for 50 microseconds (20 kHz)
        time.sleep(0.01)
