import multiprocessing

from appli.consumer import consume_data
from appli.producer import produce_data
from appli.producerSerial import serial_worker

if __name__ == "__main__":
    # queue to exchange data between producer and consumer
    queue = multiprocessing.Queue(maxsize=4)

    port = 'COM3'
    baud_rate = 460800

    serial_process = multiprocessing.Process(target=serial_worker, args=(queue, port, baud_rate))
    serial_process.start()

    # Start producer process
    # produce_process = multiprocessing.Process(target=produce_data, args=(queue,))
    # produce_process.start()

    # Start GUI process
    consume_process = multiprocessing.Process(target=consume_data, args=(queue,))
    consume_process.start()
