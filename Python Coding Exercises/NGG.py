#Next Greater Element using Stack

class Stack:
	def __init__(self):
		self.array = []

	def isEmpty(self):
		return len(self.array)==0

	def push(self,x):
		self.array.append(x)

	def pop(self):
		if self.isEmpty():
			return
		else:
			return self.array.pop()

def printNGG(arr,s):
	next = 0
	element = 0
	s.push(arr[0])
	
	for i in range(1,len(arr)):
		next = arr[i]
		
		if not s.isEmpty():
			element = s.pop()
			
			while element < next:
				print (str(element)+":"+ str(next))
				if s.isEmpty():
					break
				element = s.pop()
			
			if element > next:
				s.push(element)
		s.push(next)

	while not s.isEmpty():
		element = s.pop()
		next = -1
		print (str(element)+":"+ str(next))

#Driver Program
s = Stack()
arr = [11,10,9,3]
printNGG(arr,s)
