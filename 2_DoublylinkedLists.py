# Doubly LinkedList Example

class Head:
    def __init__(self):
        self.head_pointer = None
    
    def for_Traverse(self):
        print("TRAVERSING IN FORWARD DIRECTION")
        temp_head = self.head_pointer
        while temp_head is not None:
            print(temp_head.val)
            temp_head  = temp_head.next
    
    def rev_Traverse(self):
        print("TRAVERSING IN REVERSE DIRECTION")
        temp_head = self.head_pointer
        while temp_head.next is not None:
            #print(temp_head.val)
            temp_head  = temp_head.next
        while temp_head != None:
            print(temp_head.val)
            temp_head = temp_head.prev



class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None


# CREATION OF HEAD POINTER 
head =  Head()

# Linking Head Pointer With Node 1(n1)
head.head_pointer = Node("Mon")

# CREATING NODE OF DLL & Linking 
n2 = Node("Tue")
head.head_pointer.next = n2
n2.prev = head.head_pointer

n3 = Node("Wed")
n2.next = n3
n3.prev = n2

# TRAVERSING IN FORWARD DIRECTION
head.for_Traverse()

# TRAVERSING IN REVERSE DIRECTION
head.rev_Traverse()