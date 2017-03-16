# check if sting a is permutaion of b in O(n) using python dict
# ctci 1.2

def isPermutation(a,b):
	if len(a)!= len(b):
		return False
	d1 = {}
	for i in a:
		if d1.has_key(i):
			d1[i]+=1 
		else:
			d1[i]=1
	for i in b:
		if d1.has_key(i):
			d1[i]-=1
		else:
			return False
	for i in d1.keys():
		if d1[i] != 0:
			return False
	return True

a = "abcd"
b = "dcaba"
print isPermutation(a,b)