#palindrome permutation in python
#ctci 1.4

def palPerm(s):
	s = s.lower().split()
	s = ("").join(s)
	count = [0]*(ord('z')-ord('a')+1)
	countOdd = 0
	for i in s:
		x = ord(i)-97
		count[x]+=1
		if count[x]%2 ==1:
			countOdd+=1
		else:
			countOdd-=1
	return countOdd<=1

s = "Taco cat"
print palPerm(s)