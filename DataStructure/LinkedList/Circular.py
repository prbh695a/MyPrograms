class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class Circular:
    def __init__(self):
        self.last=None

    def addNode(self,value):
        node=Node(value)
        if(self.last==None):
            self.last=node
            node.next=self.last
        else:
            p=self.last
            while(p.next!=self.last):
                p=p.next
            p.next=node
            node.next=self.last

    def displayList(self):
        p=self.last
        while(True):
            print(p.value)
            p=p.next
            if(p==self.last):
                break

    def deleteNode(self,value):
            p=self.last
            while(p.next.value!=value):
                p=p.next
            else:
                p.next=p.next.next
                if(self.last.value==value):
                    self.last=p.next



c=Circular()
c.addNode(5)
c.addNode(6)
c.addNode(7)
c.addNode(8)
c.addNode(9)
c.addNode(10)
print("the list now is...")
c.displayList()

print("After deleting 5")
c.deleteNode(5)
c.displayList()

print("After deleting 7")
c.deleteNode(7)
c.displayList()


print("After deleting 10")
c.deleteNode(10)
c.displayList()
