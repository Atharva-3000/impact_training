# import threading
# class x(threading.Thread):
#     def run(self):
#         for p in range(101,200):
#             print(p)
#         # print(self.getName())
# class y(threading.Thread):
#     def run(self):
#         for q in range(1,100):
#             print(q)
#         # print(self.getName())
# x1=x()
# x1.start()
# x1.join()
# y1=y()
# y1.start()
# y1.join()
import time
import threading
class x(threading.Thread):
    def run(self):
        for p in range(101,151):
            print(p)
        # print(self.getName())
class y(threading.Thread):
    def run(self):
        sum=0
        for q in range(1,101):
            sum=sum+q
        # print(self.getName())
        print(sum)
class z(threading.Thread):
    time.sleep(2)
    def run(self):
        for r in range(151,201):
            print(r)
x1=x()
x1.start()
x1.join()
y1=y()
y1.start()
r1=z()
r1.start()