class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class QueueLL:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        node=Node(value)
        if self.front==None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

        self.display()

    def display(self):
        print("the current status")
        p=self.front
        while(p!=None):
            print(p.value)
            p=p.next

    def dequeue(self):
        self.front=self.front.next
        self.display()

q=QueueLL()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.dequeue()

