from threading import Thread
from time import sleep


def square_numbers():
    for i in range(1000):
        result = i * i
        sleep(1)


if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.daemon = True
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()