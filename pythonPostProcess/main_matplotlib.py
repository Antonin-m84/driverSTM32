from typing import List

import matplotlib.pyplot as plt
import numpy as np

import serial
import time

# Open the serial port
# ser.open()


def loop():
    # table of parsed values
    tableau: List[int] = []
    # memory variable of last table
    last_table_size = 0

    # disable display if first parsing
    first_time = True
    plt.ion()
    fig, ax = plt.subplots()
    plt.title("VL53L8CX 8x8 V2")
    plt.axis('off')

    def refresh_plot():
        # size should be 16 or 64 - 0 default - used for displaying and checking table
        size: int = len(tableau)

        values = []
        coordinates_x = []
        coordinates_y = []

        # if size != last_table_size:

        # should remove all texts
        ax.clear()

        # update values
        if size == 16:
            values = [
                 # Convert each element of the subset (from i to i+4) using map to int, wrapped as a list
                 list(map(int, tableau[i:i+4]))
                 # iterate from 0 to tableau length (16) step by 4
                 for i in range(0, len(tableau), 4)
            ][::-1]

            for y in range(4):
                for x in range(4):
                    ax.text(x, 3 - y, f'{tableau[y * 4 + x]}', color="black", ha="center", va="center")

            coordinates_x = list(range(4))
            coordinates_y = list(range(4))

        if size == 64:
            values = [
                 # Convert each element of the subset (from i to i+8) using map to int, wrapped as a list
                 list(map(int, tableau[i:i+8]))
                 # iterate from 0 to tableau length (64) step by 8
                 for i in range(0, len(tableau), 8)
            ][::-1]

            for y in range(8):
                for x in range(8):
                    ax.text(x, 7 - y, f'{tableau[y * 8 + x]}', color="black", ha="center", va="center")

            coordinates_x = list(range(8))
            coordinates_y = list(range(8))


        ax.pcolormesh(coordinates_x, coordinates_y, values,
          vmin=0,
          vmax=4500
        )

        # re-drawing the figure
        fig.canvas.draw()

        # to flush the GUI events
        fig.canvas.flush_events()
        fig.tight_layout()

        # Print to the console (debug)

        print_table(tableau)


    try:
        # Read and print the data from the serial port
        while True:
            # decode = convert raw signal (b'Zone;...' to encoded string ("Zone;...")
            line = ser.readline().decode("utf-8", errors="ignore")

            result = parse_line(line)

            # state machine of parsing code
            if result == -1:
                pass  # header

            elif result == -2:

                if not first_time:
                    refresh_plot()

                else:
                    first_time = False

                # new table
                tableau = []

            else:
                tableau.append(result)

            # print(cc)
    except Exception as e:
        print(e)
    finally:
        ser.close()


def print_table(table: List[int]):
    print(table)

    for i in range(len(table)):
        print(f'{table[i]:^6}', end="|")
        if (i + 1) % 4 == 0:
            print("")


def parse_line(line) -> int:
    """
    :param line:
    :return: -1 is header, -2 is new table, -3 is error
    """

    # check if 5 ; => valid line
    if line.count(";") == 5:
        if line.startswith("Zone"):
            # cas du header, ignore
            print("Got header -- Ignore")

            return -1

        if len(line) < 8 and line.startswith(";;;;;"):
            # reset table index
            # current_table_index = 0
            # tableau = ["0"] * len(tableau)
            return -2
        else:
            # line with data
            zone, nb_targets, ambient, target_status, distance, _ = line.split(";")

            return int(distance)

    else:
        print("invalid line")
        return -3


if __name__ == '__main__':
    # Create a serial object with the specified configuration
    ser = serial.Serial(
        port='COM3',
        baudrate=460800,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE
    )

    loop()