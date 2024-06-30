"""
read data from STM32 COM3 serial port and send to producer the parsed data
"""

import serial
import multiprocessing
from typing import List


def serial_worker(queue: multiprocessing.Queue, port: str, baudrate: int):
    """
    Worker function to read data from the serial port and push it to the queue.
    """

    looping = True

    def parse_line(line) -> int:
        """
        Parse a line from the serial port.

        :param line: Line read from the serial port.
        :return: Parsed integer value or special markers (-1: header, -2: new table, -3: error).
        """
        # check if line has 5 semicolons
        if line.count(";") == 5:
            if line.startswith("Zone"):
                # print("Got header -- Ignore")
                return -1

            if len(line) < 8 and line.startswith(";;;;;"):
                return -2
            else:
                zone, nb_targets, ambient, target_status, distance, _ = line.split(";")
                return int(distance)
        else:
            print(f'Invalid line : "{line.strip()}"')
            return -3

    # Create a serial object with the specified configuration
    ser = serial.Serial(
        port=port,
        baudrate=baudrate,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE
    )

    tableau: List[int] = []
    first_time = True

    try:
        # Read and parse the data from the serial port
        while looping:
            line = ser.readline().decode("utf-8", errors="ignore")
            result = parse_line(line)

            if result == -1:
                pass  # Ignore header

            elif result == -2:
                if not first_time:
                    try:
                        queue.put_nowait(tableau)
                    except:
                        pass
                else:
                    first_time = False

                # Reset table for new data
                tableau = []

            else:
                tableau.append(result)

    except Exception as e:
        print(e)

    finally:
        ser.close()


# def main():
#
#     Start the serial worker process
#
#
#     try:
#         while True:
#             # Process data from the queue
#             if not queue.empty():
#                 data = queue.get()
#                 print("Received data:", data)
#                 # Additional processing can be done here
#
#     except KeyboardInterrupt:
#         print("Terminating...")
#     finally:
#         serial_process.terminate()
#         serial_process.join()

