def acquire_gil(sleep_seconds: int) -> None:
    """
    Acquire the GIL and sleep for given seconds.

    This prevents multithreaded processing of Python code in CPython
     while this function executes.

    :raises RuntimeError: if can’t acquire GIL. (Shouldn’t happen normally.)

    Code demonstrating that it works:

        import my, threading, time

        class T(threading.Thread):
            def __init__(self, sleep_seconds):
                self.sleep_seconds = sleep_seconds
                super().__init__()

            def run(self):
                print(f"Thread {self.native_id} started")
                time.sleep(0.1)
                my.acquire_gil(self.sleep_seconds)
                print(f"Thread {self.native_id} finished")

        ts = [T(2) for _ in range(3)]  # 3 tasks that wait for 2 seconds each

        for t in ts:
            t.start()

        for t in ts:
            t.join()

        # finishes in 6 seconds instead of 2 secs if threads were concurrently processed
    """
