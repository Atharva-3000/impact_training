class test:
    def insert(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a, self.b)
    def update(self):
        self.a= self.a+10
        self.b= self.b+20
t1=test()
t1.insert(10,20)
t1.display()
t1.update()
t1.display()
t2=test()
t2.insert(300,400)
t2.display()
t2.update()
t2.display()