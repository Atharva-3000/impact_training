# def gen():
#     yield 5
#     yield 10
#     yield 15
#     yield 20
# g1=gen()
# r=next(g1)
# r1=next(g1)
# r2=next(g1)
# r3=next(g1)
# print(r,r1,r2,r3)


def gen():
    l=[15,14,13,12]
    for p in l:
        yield p
g1=gen()
for p in g1:
    print(p)