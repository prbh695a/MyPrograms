class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class Stack:
    def __init__(self):
        self.top=None

    def push(self,value):
        node=Node(value)
        if(self.top==None):
            self.top=node
        else:
            node.next=self.top
            self.top=node

    def pop(self):
        temp=None
        if(self.top!=None):
            temp=self.top.value
            self.top=self.top.next
        return(temp)

    def displayStack(self):
        p=self.top
        while(p!=None):
            print(p.value)
            p=p.next

s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
print("The stack is")
s.displayStack()
print("The popped element is",s.pop())
print("The popped element is",s.pop())
print("The popped element is",s.pop())
s.displayStack()

