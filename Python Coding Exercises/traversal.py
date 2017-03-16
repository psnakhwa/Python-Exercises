#Traversals in Binary trees

class Node:
	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None

def preOrder(root):
	if root:
		print root.val,
		preOrder(root.left)
		preOrder(root.right)

def inOrder(root):
	if root:
		inOrder(root.left)
		print root.val,
		inOrder(root.right)

def postOrder(root):
	if root:
		postOrder(root.left)
		postOrder(root.right)
		print root.val,

def levelOrder(root):
	if root is None:
		return
	queue = []
	queue.append(root)
	while queue:
		s = queue.pop(0)
		print s.val,
		if s.left:
			queue.append(s.left)
		if s.right:
			queue.append(s.right)

def levelOrderLineByLine(root):
	thisLevel = [root]
	while thisLevel:
		nextLevel = []
		for n in thisLevel:
			print n.val
			if n.left:
				nextLevel.append(n.left)
			if n.right:
				nextLevel.append(n.right)
		print
		thisLevel = nextLevel

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print "PreOrder:"
preOrder(root)
print ""

print "InOrder:"
inOrder(root)
print ""

print "PostOrder:"
postOrder(root)
print ""

print "LevelOrder:"
levelOrder(root)
print

print "LevelOrderLineByLine:"
levelOrderLineByLine(root)
