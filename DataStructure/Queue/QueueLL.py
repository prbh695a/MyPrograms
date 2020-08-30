class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class QueueLL:
    def __init__(self):
        self.rear=None
        self.front=None

    def add(self,value):
        node=Node(value)
        if(self.front==None):
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def delete(self):
        temp=self.front.value
        self.front=self.front.next
        return(temp)

    def displayQueue(self):
            p=self.front
            while(p!=None):
                print(p.value)
                p=p.next

q=QueueLL()
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