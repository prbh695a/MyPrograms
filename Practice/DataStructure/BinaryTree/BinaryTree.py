class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def addNode(self,value):
        node=Node(value)
        if(self.root==None):
            self.root=node
        else:
            current=self.root
            parent=self.root
            while(current!=None):
                parent = current
                if(current.value < node.value):
                    current=current.right
                else:
                    current=current.left
            if(parent.value<node.value):
                parent.right=node
            else:
                parent.left=node

    def displayTreePreorderIterative(self):
        current=self.root
        tempStack=[]
        tempStack.append(current)
        while(len(tempStack)!=0):
            prev=tempStack.pop()
            print(prev.value,end = ' ')
            if (prev.right!=None):
                tempStack.append(prev.right)
            if(prev.left!=None):
                tempStack.append(prev.left)

    def displayTreeInorderIterative(self):
        current=self.root
        tempStack=[]
        while(True):
            if (current!=None):
                tempStack.append(current)
                current=current.left
            elif(len(tempStack)>0):
                current=tempStack.pop()
                print(current.value,end = ' ')
                current=current.right
            else:
                break

    def displayTreePostorderIterative(self):
        current=self.root
        s1=[]
        s2=[]
        s1.append(self.root)
        while(len(s1)>0):
            temp=s1.pop()
            s2.append(temp)

            if(temp.left!=None):
                s1.append(temp.left)
            if(temp.right!=None):
                s1.append(temp.right)

        while(len(s2)>0):
            temp=s2.pop()
            print(temp.value,end= " ")


    def displayTreePreorderRecursive(self,root):
        if root:
            print(root.value,end = ' ')
            self.displayTreePreorderRecursive(root.left)
            self.displayTreePreorderRecursive(root.right)

    def diplayPreorderR(self):
        self.displayTreePreorderRecursive(self.root)

    def displayTreeInorderRecursive(self,root):
        if root:
            self.displayTreeInorderRecursive(root.left)
            print(root.value,end = ' ')
            self.displayTreeInorderRecursive(root.right)

    def diplayInorderR(self):
        self.displayTreeInorderRecursive(self.root)

    def displayTreePostorderRecursive(self,root):
        if root:
            self.displayTreePostorderRecursive(root.left)
            self.displayTreePostorderRecursive(root.right)
            print(root.value,end = ' ')

    def diplayPostorderR(self):
        self.displayTreePostorderRecursive(self.root)


b=BinaryTree()
b.addNode(100)
b.addNode(90)
b.addNode(80)
b.addNode(70)
b.addNode(88)
b.addNode(95)
b.addNode(93)
b.addNode(97)
b.addNode(150)
b.addNode(160)
b.addNode(158)
b.addNode(170)
print("\n+++++++++++++++PreOrder+++++++++++++++")
print("root->left->right")
b.displayTreePreorderIterative()
print(" ")
b.diplayPreorderR()

print("\n+++++++++++++++InOrder+++++++++++++++")
print("left->root->right")
b.displayTreeInorderIterative()
print(" ")
b.diplayInorderR()

print("\n+++++++++++++++PostOrder+++++++++++++++")
print("left->right->root")
b.displayTreePostorderIterative()
print(" ")
b.diplayPostorderR()
