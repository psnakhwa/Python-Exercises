#intersection of ll
#ctci 2.7

class Node:
	
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None



def findIntersection(head1,head2):
	currA,currB = head1,head2
	lenA,lenB = 0,0
	#Get lengths of two linked lists
	while currA:
		lenA+=1
		currA = currA.next
	while currB:
		lenB+=1
		currB=currB.next
	#Set currA and currB back to head1 and head2
	currA,currB = head1,head2
	#make the start of the longer LL traverse till both linked lists become equal
	if lenA > lenB:
		for __ in range(lenA-lenB):
			currA=currA.next
	elif lenB > lenA:
		for __ in range(lenB-lenA):
			currB = currB.next
	#The place where currA and currB meets is the intersection
	while currA != currB and currA and currB:
		currA = currA.next
		currB = currB.next
	
	if currA and currB:
		return currA.data
	else:
		print "no intersection"
		return 

l1 = LinkedList()
l1.head1 = Node(1)
l1.head1.next = Node(2)
l1.head1.next.next = Node(3)
l1.head1.next.next.next = Node(4)
l1.head1.next.next.next.next = Node(5)

l2 = LinkedList()
l2.head2 = Node(10)
l2.head2.next = Node(20)
#l2.head2.next.next = l1.head1.next.next

print findIntersection(l1.head1,l2.head2)
