import threading
import time
class x(threading.Thread):
    def run(self):
        time.sleep(1)
        for p in range(1,11):
            print("Rama Thread")
        # print(self.getName())
class y(threading.Thread):
    def run(self):
        for q in range(1,6):
            print("Seetha Thread")
            time.sleep(2)
        # print(self.getName())
x1=x()
x1.start()
y1=y()
y1.start()