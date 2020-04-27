class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class CL:
    def __init__(self):
        self.last=None

    def insertnode(self,value):
        node=Node(value)
        if self.last == None:
            self.last=node
            node.next=self.last
        else:
            node.next=self.last.next
            self.last.next=node
            self.last=node
        c.display()

    def display(self):
        p=self.last.next
        print ("The list now is:")
        while(p!=None):
            print(p.value)
            p=p.next
            if (p==self.last.next):
                break;

    def deletenode(self):
        p=self.last.next
        while(p!=None):
            p=p.next
            if (p.next==self.last):
                p.next=self.last.next
                self.last=p
                break;
        c.display()

c=CL()
c.insertnode(1)
c.insertnode(2)
c.insertnode(3)
c.insertnode(4)
c.insertnode(5)
c.insertnode(6)
c.insertnode(7)

c.deletenode()
c.deletenode()
c.deletenode()
c.deletenode()