#Infix to postfix
class Conversion():

	def __init__(self,capacity):
		self.capacity = capacity
		self.top = -1
		self.array = []				#Stack Array
		self.output = []			#Postfix Array
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

	def isEmpty(self):
		return True if self.top == -1 else False

	def push(self, operator):
		self.top+= 1
		self.array.append(operator)

	def pop(self):
		if not self.isEmpty():
			self.top-=1
			return self.array.pop()
		else:
			return '$'

	def peek(self):
		return self.array[-1]

	def isOperand(self,ch):
		return ch.isalpha()

	def notGreater(self,i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a<=b else False
		except KeyError:
			return False

	def infixToPostfix(self,exp):
		for i in exp:
			
			if self.isOperand(i):										#Operand is Encountered
				self.output.append(i)

			elif i == '(':												#'(' is Encountered
				self.push(i)

			elif i == ')':												#')' is Encountered
				while not self.isEmpty() and self.peek() !='(':
					a=self.pop()
					self.output.append(a)
				if not self.isEmpty() and self.peek() != '(':
					return -1
				else:self.pop()

			else:														#Operator is encountered
				while not self.isEmpty() and self.notGreater(i):
					b = self.pop()
					self.output.append(b)
				self.push(i)

		while not self.isEmpty():										#Pop out remaining operators from the stack
			self.output.append(self.pop())

		print "".join(self.output)

exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)

