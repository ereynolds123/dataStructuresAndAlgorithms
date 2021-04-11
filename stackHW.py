#Implementing a Stack with Linked List
#Create a  class 
class Stack:
    #Create a Node
    class Node:
        #Initialize the function so it referenses the element in the node and the next node address 
        def __init__(self, element, next):
            self.element = element
            self.next= next
            
    #Initialize the first node
    def __init__(self):
        self.head =None
        self.size =0
        
    #Gets the length of the linked list   
    def __len__(self):
        return self.size
    
    #Determines the size of the stack
    def isEmpty(self):
        if self.size == 0:
            print("Stack is empty")
        else:
            print ("Stack is not empty. Stack has {} elements".format(self.size))
        return self.size ==0
    
    
    #Creates a new node, increases the size of the stack by one
    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size +=1
    
    #Check if stack is empty. If empty, raise and error.
    #Otherwise, decrease the size of stack. Get new head
    def pop(self, element):
        if self.isEmpty():
            print("The stack is empty")
        else:
            self.size -=1
            headOfStack =self.head.element
            self.head = self.head.next
            return headOfStack
        
myStack = Stack()
myStack.push(11)
myStack.isEmpty()
myStack.push(12)
myStack.isEmpty()


#https://www.screencast.com/t/CetRvqsW2L Video