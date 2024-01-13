ls=[]
def adder(i):
    if(i==0):
        return
    else:
        ls.append(i)
        adder(i=i-1)
    return ls
print(*adder(5))