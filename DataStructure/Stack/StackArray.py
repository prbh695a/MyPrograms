class Stack:
    def __init__(self):
        self.items=[None] * 10
        self.count=-1

    def push(self,value):
        self.count=self.count+1
        self.items[self.count]=value

    def pop(self):
        temp=self.items[self.count]
        self.items[self.count]=None
        self.count=self.count-1

        return temp

    def displayStack(self):
        print(self.items)

def main():
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
    s.displayStack()
    print("The popped element is",s.pop())
    print("The popped element is",s.pop())
    print("The popped element is",s.pop())
    s.displayStack()

if __name__ == "__main__":
    main()