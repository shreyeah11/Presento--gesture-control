import time

class Timer:
    def __init__(self):
        self.last_time = time.time()

    def should_trigger(self, delay):
        current = time.time()
        if current - self.last_time > delay:
            self.last_time = current
            return True
        return False
