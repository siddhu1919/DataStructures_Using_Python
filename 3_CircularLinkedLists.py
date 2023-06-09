# Circular linked lists Example

class Head:
    def __init__(self):
        self.head_pointer = None

    # TRAVERSE FUNCTION
    def traverse(self):
        temp_head = self.head_pointer
        if temp_head == None:
            print("Node Unavailable")
            
        else:
            while True:
                print(temp_head.val)
                temp_head = temp_head.next
                if temp_head == self.head_pointer:
                    break



class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None


head =  Head()

head.head_pointer = Node("Mon")
n2 = Node("Tue")
head.head_pointer.next = n2     
n3 =  Node("Wed")
n2.next = n3
n3.next = head.head_pointer

# TRAVERSE FUNCTION
head.traverse()



