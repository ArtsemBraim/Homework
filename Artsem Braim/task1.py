import time
import threading


class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            time.sleep(5)
            print(f"Philosopher {self.index} is hungry.")
            self.dine()

    def dine(self):
        fork1 = self.left_fork
        fork2 = self.right_fork
        while self.running:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
        else:
            return
        self.dining()

        fork2.release()
        fork1.release()

    def dining(self):
        print(f"Philosopher {self.index} starts eating.")
        time.sleep(2)
        print(f"Philosopher {self.index} finishes eating.")


if __name__ == "__main__":
    forks = [threading.Lock() for i in range(5)]

    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5])
                    for i in range(5)]

    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(15)
    Philosopher.running = False
    print("Spaghetti is over")
