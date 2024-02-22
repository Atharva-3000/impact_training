class pq:
    def __init__(self):
        self.queue=[]
    def push(self,data):
        self.queue.append(data)
    def display(self):
        print(self.queue)
    def delete(self):
        self.queue.sort()
        print("Deleted element is: ",self.queue.pop(0))
    def deleteAscending(self):
        self.queue.sort(reverse=True)
        print("Deleted element is: ",self.queue.pop(0))
        
p1=pq()
p1.push(10)
p1.push(20)
p1.push(30)
p1.push(40)
p1.display()
p1.delete()
p1.deleteAscending()