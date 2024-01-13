class Test:
    def op(self,d,*a):
        if(d=="int"):
            s1=0
        else:
            s1=''
        for p in a:
            s1=s1+p
        print(s1)
t1=Test()
t1.op("Krishna","Rama","Hanumana")