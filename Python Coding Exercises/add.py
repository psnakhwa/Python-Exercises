	class Node:
	
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self,data):
		n = Node(data)
		n.next = self.head
		self.head = n


	def addLinkedList(self,head1,head2):
		carry = 0
		prev = None
		while head1 or head2:

			a = 0 if head1 is None else head1.data
			b = 0 if head2 is None else head2.data
			Sum = a+b+carry
			total = Sum%10
			new_node = Node(total)
			if self.head is None:
				self.head = new_node
			else:
				prev.next = new_node
			carry = Sum/10
			prev = new_node
			if head1:	
				head1 = head1.next
			if head2:
				head2 = head2.next
		if carry>0:
			new_node = Node(carry)
			prev.next = new_node



	def printList(self):
		temp = self.head
		while temp:
			print temp.data,
			temp = temp.next

l1 = LinkedList()
l2 = LinkedList()
l1.push(6)
l1.push(4)
l1.push(9)
l2.push(4)
l2.push(4)
l2.push(8)
l3 = LinkedList()
l3.addLinkedList(l1.head,l2.head)
l3.printList()

