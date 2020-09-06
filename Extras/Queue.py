class Queue:
    def __init__(self):
        self.item=[]

    def enqueue(self,value):
        self.item.append(value)
        self.display()

    def dequeue(self):
        return self.item.pop(0)

    def display(self):
        print("The Queue Status is ",*self.item)

q=Queue()
print("Enqueuing in the queue")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Dequeuing in the queue")
q.dequeue()
q.display()
q.dequeue()
q.display()