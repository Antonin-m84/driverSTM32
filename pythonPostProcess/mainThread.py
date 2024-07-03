import threading
import queue

from appli.consumer import consume_data
from appli.producerRandom import produce_data
from appli.producerSerial import serial_worker
from appli.producerReplay import replay_data

if __name__ == "__main__":
    # queue to exchange data between producer and consumer
    queue = queue.Queue(maxsize=4)

    port = 'COM3'
    baud_rate = 460800

    serial_thread = threading.Thread(target=replay_data, args=(queue, port, baud_rate))
    serial_thread.start()

    # Start producer thread
    # produce_thread = threading.Thread(target=produce_data, args=(queue,))
    # produce_thread.start()

    # Start GUI thread
    consume_thread = threading.Thread(target=consume_data, args=(queue,))
    consume_thread.start()
