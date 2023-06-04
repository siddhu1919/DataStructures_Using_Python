# Circular doubly linked lists.

class Head:
    def __init__(self):
        self.head_pointer = None

    # FORWARD TRAVERSE FUNCTION
    def for_Traverse(self):
        print("TRAVERSING IN FORWARD DIRECTION")
        temp_head = self.head_pointer
        if temp_head == None:
            print("Node Unavailable")
            
        else:
            while True:
                print(temp_head.val)
                temp_head = temp_head.next
                if temp_head == self.head_pointer:
                    break

    # REVERSE TRAVERSE FUNCTION            
    def rev_Traverse(self):
        print("TRAVERSING IN REVERSE DIRECTION")
        temp_head = self.head_pointer
        while temp_head.next is not head.head_pointer:
            #print(temp_head.val)
            if temp_head.next != head.head_pointer:
                temp_head  = temp_head.next

        while temp_head != head.head_pointer:
            print(temp_head.val)
            temp_head = temp_head.prev
            if temp_head == head.head_pointer:
                print(temp_head.val)
                break

class Node:
    def __init__(self,val=None):
        self.val=val
        self.prev = None
        self.next = None


# MAIN CODING

# CREATING HEAD POINTER 
head = Head()
head.head_pointer = Node("MON")
n2 = Node("TUE")
head.head_pointer.next = n2
n2.prev = head.head_pointer

n3 = Node("WED")
n3.prev =  n2
n2.next =  n3
n3.next = head.head_pointer
head.head_pointer.prev = n3


# TRAVERSE FUNCTION
head.for_Traverse()

head.rev_Traverse()

           