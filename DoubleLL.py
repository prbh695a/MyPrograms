class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DL:
    def __init__(self ):
        self.start = None

    def insertnode(self,value):
        node= Node(value)
        if(self.start == None):
            self.start=node
        else:
            temp = self.start
            while(temp.next != None):
                temp=temp.next
            temp.next=node
            node.prev=temp
        d.displaylist()

    def displaylist(self):
         temp=self.start
         print("The list now is")
         while(temp !=None):
             print(temp.value)
             temp=temp.next

    def deletefromstart(self):
        p = self.start
        self.start=p.next
        self.start.prev=None
        d.displaylist()

    def deletefromend(self):
        p = self.start
        while(p.next!= None):
            p=p.next
        p.prev.next=None
        p.prev=None
        d.displaylist()

d = DL()
d.insertnode(5)
d.insertnode(6)
d.insertnode(7)
d.insertnode(8)
d.insertnode(9)
d.insertnode(10)
d.deletefromstart()
d.deletefromstart()
d.deletefromend()
d.deletefromend()


