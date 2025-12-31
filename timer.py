import time

class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        elapsed = (time.time() - self.start) * 1000
        print(f"{self.name}: {elapsed:.2f} ms")
