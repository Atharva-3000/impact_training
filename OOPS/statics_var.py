class test:
    a=1000
    b=2000
    def display(self):
        print(test.a,test.b)
    def update(self):
        test.a=test.a+10
        test.b=test.b+20
        
#static variables can be used using class name
t1= test()    
t1.display()
t1.update()
t1.display()
t2=test()
t2.display()
t2.update()
t2.display()