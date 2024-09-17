import multiprocessing
from datetime import datetime
from appli.consumer import consume_data
from appli.producerRandom import produce_data
from appli.producerSerial import serial_worker

if __name__ == "__main__":
    # queue to exchange data between producer and consumer
    queue = multiprocessing.Queue(maxsize=4)

    port = 'COM3'
    baud_rate = 460800

    serial_process = multiprocessing.Process(target=serial_worker, args=(queue, port, baud_rate))
    serial_process.start()

    # Add current date and time to the log file
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"D:/Documents/Mémoire/pythonPostProcess/Sessions Logs/session_log_{now}.csv"

    # Start GUI process
    consume_process = multiprocessing.Process(target=consume_data, args=(queue, True, ))
    consume_process.start()

