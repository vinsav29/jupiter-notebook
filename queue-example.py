from threading import Thread, Lock, current_thread
from queue import Queue
from time import sleep

class Queuer():
    q = None
    lock = None

    def __init__(self):
        q = Queue()
        lock = Lock()

        get = Thread(name=f"GetThread", target=self.getter, args=(q, lock))
        put = Thread(name=f"PutThread", target=self.putter, args=(q, lock))
        get.daemon = True  # dies when the main thread dies
        put.daemon = True
        get.start()
        put.start()

    def getter(self, q, lock):
        while True:
            value = q.get()  # blocks until the item is available

            # do stuff...
            with lock:
                # prevent printing at the same time with this lock
                print(f"in {current_thread().name} got {value}")
                sleep(1)
            # ...

            # For each get(), a subsequent call to task_done() tells the queue
            # that the processing on this item is complete.
            # If all tasks are done, q.join() can unblock
            q.task_done()

    def putter(self, q, lock):
        for readbyte in range(100):
            with lock:
                q.put(readbyte)
                print("put: {}".format(readbyte))
            # sles

if __name__ == '__main__':
    q = Queuer()

    # fill the queue with items
    # for x in range(10):
    #     q.put(x)

    # while True:
    #     sleep(1)
    #     q.put(0)
    # q.join()  # Blocks until all items in the queue have been gotten and processed.
    while True:
        pass
    print('main done')