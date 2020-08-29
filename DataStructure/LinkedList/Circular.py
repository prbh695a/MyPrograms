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
        else:
            p=self.last
            while(p.next!=None):
                p=p.next
            p.next=node
            node.next=self.last

    def displayList(self):

