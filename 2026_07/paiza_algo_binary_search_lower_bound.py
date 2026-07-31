q = int(input()) 
stack = [""] * 255 
stack_size = 0 

for i in range(q): 
query = input().split()
if query[0] == "1":
	stack[stack_size] = query[1] 
	stack_size += 1
else: 
	print(stack[stack_size-1]) 
	stack_size -= 1 
if stack_size == 0: 
	print() 
else: 
for j in range(stack_size):
	 print(stack[j])