#is rotation

def isRotation(s1,s2):
	return len(s1)==len(s2) and s1 in 2*s2

print isRotation("aba","abb")
s2 = "aba"
print 2*s2