#Reverse an array

import sys

def reverse(a,start,end):
	if start>=end:
		return
	temp = a[start]
	a[start] = a[end]
	a[end] = temp
	reverse(a,start+1,end-1)


a = [1,2,3,4,5,6]
print " ".join(str(p) for p in a)
reverse(a,0,5)
print " ".join(str(p) for p in a)