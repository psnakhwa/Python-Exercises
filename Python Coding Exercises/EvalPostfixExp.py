#Evaluating Postfix Expression

class Evaluate:
	def __init__(self,capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []

	def isEmpty(self):
		return True if self.top == -1 else False

	def push(self,digit):
		self.top+=1
		self.array.append(digit)

	def pop(self):
		if not self.isEmpty():
			self.top-=1
			return self.array.pop()
		else:
			return '$'

	def peek(self):
		return self.array[-1]

	def evalPostfix(self,exp):
		for i in exp:
			if i.isdigit():
				self.push(i)

			else:
				secondval = self.pop()
				firstval = self.pop()
				self.push(str(eval(firstval+i+secondval)))

		return int(self.pop())

exp = "231*+9-"
obj = Evaluate(len(exp))
print "Value of %s is %d" %(exp, obj.evalPostfix(exp))