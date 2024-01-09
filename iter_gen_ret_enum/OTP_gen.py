#wap to generate 4 random otps within the range of 1000, to 10000
import random
for i in range(0,4):
    print(random.randint(1000,10000),end=" ")
    
    
# or
def gen():
    i=1
    while(i<4):
        d=random.randint(1000,10000)
        yield d
        i=i+1
g1=gen()
print()                             
for p in g1:
    print(p)