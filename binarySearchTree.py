#Tree node class
class TreeNode:
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild
    
    def getRootVal(self):
        return self.val

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
            
     


#Binary search tree class
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
            self.size = self.size + 1
    #Adds to the tree
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.getLeftChild():
               self._put(key,val,currentNode.leftChild)
            else:
               currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.getRightChild():
               self._put(key,val,currentNode.rightChild)
            else:
               currentNode.rightChild = TreeNode(key,val,parent=currentNode)
               
#Preorder traversal 
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
        
#Postorder traversal
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
        
#Inorder traversal       
def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

#Prints the tree 
def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

#Do a binary search tree
def main():
    binaryTree = BinarySearchTree()
    binaryList = [50, 30, 23, 11, 25, 35, 31, 42, 70, 80, 73, 85]
    
    for i in range((len(binaryList))):
        binaryTree.put(binaryList[i], binaryList[i])
        
    inorder(binaryTree.root)

main()
# https://www.screencast.com/t/NZszMJCCEF