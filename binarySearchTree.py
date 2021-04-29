#Tree node class
class TreeNode:
    #Initialize the tree
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
    #Returns the value of the tree
    def getVal(self):
        return self.val
   
    def getKey(self):
        return self.key
    #Tells if you are a left child of some other node
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)


    def hasBothChildren(self):
        return self.rightChild and self.leftChild


#Binary search tree class
#Maps keys to values 
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0


    def __len__(self):
        return self.size

    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
            self.size = self.size + 1
            
    #Adds to the tree
    def _put(self,key,val,currentNode):
        #print("Debug", key, val)
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
        print(tree.getVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
        
#Postorder traversal
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getVal())
        
#Inorder traversal       
def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getVal())
      inorder(tree.getRightChild())
      


#Do a binary search tree
def main():
    binaryTree = BinarySearchTree()
    binaryList = [50, 30, 23, 11, 25, 35, 31, 42, 70, 80, 73, 85]
    
    for i in range((len(binaryList))):
        binaryTree.put(binaryList[i], binaryList[i])
        
    inorder(binaryTree.root)


# https://www.screencast.com/t/NZszMJCCEF