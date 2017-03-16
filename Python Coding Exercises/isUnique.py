# check if all characters in a string are unique in python
#ctci 1.1

def isUnique(s):
	return len(set(s))==len(s)
#will return False
s = "abdac"
print isUnique(s)
#will return True
s = "abdc"
print isUnique(s)