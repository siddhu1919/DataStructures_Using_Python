# Stack Implementation Using Python
#Operations :
# 1. Push()
# 2. Pop()
# 3. stack_Print()
# 4. isEmpty()
# 5.IsFull()
class stack:
		Stack = [] 
		size = 0
		
		def __init__(self):
			type(self).size = int(input("Enter The Size Of Stack : ") )
	
	
# isEmpty Method 

def isEmpty(temp_stack):
	if len(temp_stack.Stack) == 0:
		return 1
	else:
		return 0


def isFull(temp_stack):
	if len(temp_stack.Stack) == stack.size:
		return 1
	else:
		return 0
		
def stack_Print(temp_stack):
	print (temp_stack.Stack)

def pop(temp_stack):
	if isEmpty(temp_stack)!=1:
		return temp_stack.Stack.pop()
	else :
		print ("Stack Is Empty")

def push(temp_stack,val):
	if isFull(temp_stack) !=1:
		temp_stack.Stack.append(val)
	else:
		print("Stack is Full")	

S = stack()
#-----------------------Test Case -----------------------
#print(len(S.Stack))
#print(len(S.Stack))
#print(S.size)
#-----------------------Test Case -----------------------

isEmpty(S)
isFull(S)

push(S,2)
push(S,4)

stack_Print(S)

pop(S)
pop(S)
stack_Print(S)
		