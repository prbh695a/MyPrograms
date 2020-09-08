class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value=value

class Double:
    def __init__(self):
        self.start=None

    def addNode(self,value):
        node=Node(value)
        if(self.start==None):
            self.start=node
        else:
            p=self.start
            while(p.next!=None):
                p=p.next
            p.next=node
            node.prev=p

    def displayList(self):
        p=self.start
        while(p!=None):
            print(p.value)
            p=p.next

    def deleteNode(self,value):
        if(self.start.value==value):
            self.start=self.start.next
            self.prev=None
        else:
            p=self.start
            while(p.next.value!=value):
                p=p.next
            temp=p.next.prev
            p.next=p.next.next
            temp=p

d=Double()
d.addNode(5)
d.addNode(6)
d.addNode(7)
d.addNode(8)
d.addNode(9)
d.addNode(10)
d.displayList()

print("After deleting 5")
d.deleteNode(5)
d.displayList()

print("After deleting 7")
d.deleteNode(7)
d.displayList()


print("After deleting 10")
d.deleteNode(10)
d.displayList()





