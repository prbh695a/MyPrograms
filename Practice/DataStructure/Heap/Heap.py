class Heap:
    def __init__(self):
        self.items=[None]*20
        self.items[0]=999999
        self.n=0

    def addHeap(self,value):
        self.n=self.n+1
        self.items[self.n]=value
        self.restore(self.n)


    def restore(self,index):
        tempVal=self.items[index]
        parent=index // 2

        while(self.items[parent]<tempVal):
            self.items[index]=self.items[parent]
            index=parent
            parent=parent//2

        self.items[index]=tempVal

    def displayHeap(self):
        print(self.items)

h=Heap()
h.addHeap(85)
h.addHeap(70)
h.addHeap(55)
h.addHeap(56)
h.addHeap(40)
h.addHeap(42)
h.addHeap(33)
h.addHeap(16)
h.addHeap(28)
h.addHeap(19)
h.addHeap(20)
h.addHeap(25)
h.addHeap(80)
h.displayHeap()
