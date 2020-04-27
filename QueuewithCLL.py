class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class Queue:
    def __init__(self):
        self.rear=None

    def enqueue(self,value):
        node=Node(value)
        if(self.rear==None):
            self.rear=node
            node.next=self.rear
        else:
            node.next=self.rear.next
            self.rear.next=node
            self.rear=node

        self.display()
    def dequeue(self):
        p=self.rear.next
        self.rear.next=p.next
        self.display()

    def display(self):
        p=self.rear.next
        print("The Current Status")
        while(p!=None):
            print(p.value)
            p=p.next
            if(p==self.rear.next):
                break

q=Queue()
print("Enqueuing")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Dequeuing")
q.dequeue()
q.dequeue()


