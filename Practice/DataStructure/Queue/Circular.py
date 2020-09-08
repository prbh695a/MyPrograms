class Circular:
    def __init__(self):
        self.items=[None]* 10
        self.count=0
        self.front=0

    def add(self,value):
        position=(self.front+self.count)%10
        self.items[position]=value
        self.count=self.count+1

    def delete(self):
        temp=self.items[self.front]
        self.items[self.front]=None
        self.front=(self.front+1)%10
        self.count=self.count-1
        return temp

    def displayQueue(self):
        print(self.items)

q=Circular()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)
q.add(6)
q.add(7)
q.add(8)
q.add(9)
q.add(10)
print("The queue is")
q.displayQueue()
print("After deleting",q.delete())
q.displayQueue()
print("After deleting",q.delete())
q.displayQueue()
print("After deleting",q.delete())
q.displayQueue()
print("After deleting",q.delete())
q.displayQueue()
print("After deleting",q.delete())
q.displayQueue()

q.add(1)
q.add(2)
q.add(3)
q.add(4)
print("The queue is")
q.displayQueue()