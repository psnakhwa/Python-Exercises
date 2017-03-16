#create minimum BST from a given sorted array
#ctci 4.2

class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

def createMinBST(arr,start,end):
	if start>end:
		return
	mid = (start+end)/2
	n = TreeNode(arr[mid])
	n.left = createMinBST(arr,start,mid-1)
	n.right = createMinBST(arr,mid+1,end)
	return n

def inOrder(n):
	if n:
		inOrder(n.left)
		print n.val,
		inOrder(n.right)

n = createMinBST([1,2,3,4,5],0,4)
inOrder(n)