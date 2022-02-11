import threading
import time

import my


def test_acquire_gil():

    class T(threading.Thread):
        def __init__(self, sleep_time):
            self.sleep_time = sleep_time
            super().__init__()

        def run(self):
            time.sleep(0.1)
            my.acquire_gil(self.sleep_time)

    num_threads = 2
    sleep_sec = 1
    threads = [T(sleep_sec) for _ in range(num_threads)]
    t0 = time.time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed_time = time.time() - t0
    assert (exp := num_threads * sleep_sec) < elapsed_time < exp + 0.2
