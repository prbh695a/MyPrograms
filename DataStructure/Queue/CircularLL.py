class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class CircularLL:
    def __init__(self):
        self.rear=None


    def add(self,value):
        node=Node(value)
        if(self.rear == None):
            self.rear=node
            node.next=self.rear
        else:
            node.next=self.rear.next
            self.rear.next=node
            self.rear=node

    def delete(self):
        temp=self.rear.next
        self.rear.next=temp.next
        temp.next=None
        return(temp.value)

    def displayQueue(self):
        p=self.rear.next
        while(True):
            print(p.value)
            p=p.next
            if(p==self.rear.next):
                break

q=CircularLL()
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