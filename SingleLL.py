class Node:
    def __init__(self, value):
        self.next=None
        self.value=value

class SingleLL:
    def __init__(self):
        self.start=None

    def addNode(self, value):
        node = Node(value)
        # Means its a first node
        if(self.start==None):
            self.start=node
        # Need to go until end of the list
        else:
            prev = self.start
            while(prev.next!=None):
                prev=prev.next
            prev.next=node

    def displayList(self):
        prev=self.start
        print("the List is:")
        while(prev != None):
            print(prev.value)
            prev=prev.next

    def deleteNodeFromStart(self):
        prev=self.start
        self.start=prev.next

    def deleteNodeFromEnd(self):
        prev = self.start
        temp=prev
        while (prev.next != None):
            temp=prev
            prev = prev.next
        temp.next=None


s = SingleLL()
s.addNode(5)
s.addNode(6)
s.addNode(7)
s.addNode(8)
s.addNode(9)
s.addNode(10)
s.addNode(11)
s.displayList()
s.deleteNodeFromStart()
s.displayList()
s.deleteNodeFromStart()
s.displayList()
s.deleteNodeFromEnd()
s.displayList()
s.deleteNodeFromEnd()
s.displayList()





