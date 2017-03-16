class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LL:
	def __init__(self):
		self.head = None

	def push(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def printMiddle(self):
		slow = self.head
		fast = self.head
		if self.head is not None:
			while fast and fast.next:
				slow = slow.next
				fast = fast.next.next

		print slow.data

l = LL()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
l.printMiddle()