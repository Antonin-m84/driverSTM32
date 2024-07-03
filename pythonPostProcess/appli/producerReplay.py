import time
import multiprocessing
from typing import List

def replay_data(queue: multiprocessing.Queue):
    with open('C:\\Workspace\\CubeIDE_F401RE_Example_I2C\\pythonPostProcess\\session_log.txt', 'r') as file:
        while True:
            # Read values from the file
            line = file.readline()
            if not line:
                break  # End of file

            values = list(map(int, line.split()))
            queue.put(values)

            # Simulate high frequency by waiting for 50 microseconds (20 kHz)
            time.sleep(1)
