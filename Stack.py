class emptyexceptionError(Exception):
    #print("Problem executing pop")
    pass

class stack:
    def __init__(self):
        self.item = []

    def isempty(self):
        return self.item == []

    def push(self,value):
        self.item.append(value)

    def pop(self):
        if self.isempty():
            raise emptyexceptionError("list is empty")
        else:
            return self.item.pop()

    def display(self):
        print("The Stack Status is", *self.item)

s=stack()
#s.pop()

print("Pushing elements")
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.display()
print("Popping elements")
s.pop()
s.pop()
s.display()
