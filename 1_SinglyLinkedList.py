# Singly Linked_list Example


class node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

class head_pointer:
    def __init__(self):
        self.head_pointer=None

    def print_data(self):
        temp_val = self.head_pointer
        while temp_val is not None:
            print(temp_val.val)
            temp_val = temp_val.next


hp = head_pointer()

hp.head_pointer = node("SID")
n2=node("SIDDHU")
n3=node("SIDDHARTH")

hp.head_pointer.next=n2
n2.next = n3

hp.print_data()


