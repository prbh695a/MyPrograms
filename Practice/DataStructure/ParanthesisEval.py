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

def evalExpression(expression):
    for i in expression:
        if i in "({[" :
            #print("Pushing to stack",i)
            s.push(i)
        elif i in ")}]" :
            temp=s.pop()
            #print("Popping from stack",temp,i)
            res=matchParanthesis(i,temp)
            #print(res)
            if res==False:
                print("invalid expression")
                return()
    if(s.pop()!=None):
        print("invalid expression")
        return ()
    print("Expression is valid")

def matchParanthesis(left,right):
    #print(left,right)
    if left == ")" and right == "(":
        return True
    elif left == "}" and right == "{":
        return True
    elif left == "]" and right == "[":
        return True
    else:
        return False





s=Stack()
expression="[{{{()()()}}}{}()]"
evalExpression(expression)