#Print binary tree in Vertical order

class Node:
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None

def getVertOrder(root,hd,m):
	if root is None:
		return

	try:
		m[hd].append(root.key)
	except:
		m[hd] = [root.key]

	getVertOrder(root.left,hd-1,m)
	getVertOrder(root.right,hd+1,m)

def printVertOrder(root):
	m = dict()
	hd = 0
	getVertOrder(root,hd,m)
	for idx,val in enumerate(sorted(m)):
		for i in m[val]:
			print i,
		print

#Driver Program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print "Vertical order traversal is"
printVertOrder(root)