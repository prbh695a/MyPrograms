class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class Single:
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

    def displayList(self):
        p=self.start
        while(p!=None):
            print(p.value)
            p=p.next

    def deleteNode(self,value):
        if(self.start.value==value):
            self.start=self.start.next
        else:
            p=self.start
            while(p.next.value!=value):
                p=p.next
            p.next=p.next.next


s=Single()
s.addNode(5)
s.addNode(6)
s.addNode(7)
s.addNode(8)
s.addNode(9)
s.displayList()

print("After deleting 5")
s.deleteNode(5)
s.displayList()

print("After deleting 9")
s.deleteNode(9)
s.displayList()

print("After deleting 7")
s.deleteNode(7)
s.displayList()
