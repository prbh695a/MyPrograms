class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class stackLL:
    def __init__(self):
        self.top=None

    def push(self,value):
        print("Pushing ",value)
        node=Node(value)
        node.next=self.top
        self.top=node
        self.display()

    def pop(self):
        p=self.top.value
        self.top=self.top.next
        print("poped ",p)
        self.display()
        return p

    def display(self):
        print("Current Stack Status")
        p=self.top
        while(p!=None):
            print(p.value)
            p=p.next

s=stackLL()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.pop()