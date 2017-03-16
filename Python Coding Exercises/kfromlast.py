#ctci 2.2
#kth from last

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

	def kthlast(self,k):
		p1 = self.head
		p2 = self.head
		for __ in range(k):
			if p2 is None:
				return False
			p2 = p2.next

		while p2:
			p1 = p1.next
			p2 = p2.next

		return p1.data

	def deletenode(self,n):
		if n is None or n.next is None:
			print "cannot delete"
			return False
		next_node = n.next
		n.data = next_node.data
		n.next = next_node.next
		return True

	def printlist(self):
		temp = self.head
		while temp:
			print temp.data,
			temp = temp.next

	def partition(self,key):
		pre = self.head
		post = self.head
		node = self.head
		while node:
			next = node.next
			if node.data <key:
				node.next = pre
				pre = node
			else:
				post.next = node
				post = node
			node = next
		post.next = None
		self.head = pre


l = LL()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.push(4)
l.push(5)
l.printlist()
#k = 2
#print l.kthlast(k)
#l.deletenode(l.head.next.next.next.next)
l.partition(3)
print
l.printlist()