#Implement a Queue

#Create a  class 
class Queue:
    #Create a Node
    class Node:
        #Initialize the function so it referenses the element in the node and the next node address 
        def __init__(self, element, next):
            self.element = element
            self.next= next
            
    #Initialize the first node
    def __init__(self):
        self.head =None
        self.tail = None
        self.size =0
    
        
    #Gets the length of the linked list   
    def __len__(self):
        return self.size
    
    #Determines the size of the stack
    def isEmpty(self):
        if self.size == 0:
            print("Queue is empty")
        else:
            print ("Queue is not empty.Queue has {} elements".format(self.size))
        return self.size ==0
    
    #Enqueue to the back of the queue
    def enqueue(self, element):
        new = self.Node(element, None) #This becomes the tial element.Points to None
        if self.isEmpty():
            self.head = new #If queue is empty, the element becomes the head
        else:
            self.tail.next= new #Otherwise add to the tail
            
        
    #Dequeue at the front of the queue
    def dequeue(self, element):
        #If queue is empty, print an error
        if self.isEmpty():
            print("The queue is empty")
     
        
        headOfStack =self.head.element
        self.head = self.head.next
        self.size -=1
        if self.isEmpty():
            self.tail = None #If the queue is empty, the new tail is establishd
        return headOfStack
    
myQueue= Queue()
myQueue.isEmpty()
myQueue.dequeue(1)
myQueue.isEmpty()


#https://www.screencast.com/t/BV5JAocbn  Video