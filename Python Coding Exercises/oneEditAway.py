# check if second string is one edit away from first string 
#ctci 1.5

def oneEditReplace(s1,s2):
	foundDiff = False
	for i in range(len(s1)):
		if s1[i]!=s2[i]:
			if foundDiff:
				return False
			foundDiff = True
	return True

def oneEditInsert(big,small):
	idx1 = 0
	idx2 = 0
	while idx1<len(big) and idx2<len(small):
		if big[idx1]!=small[idx2]:
			if idx1!=idx2:
				return False
			idx1 = idx1 + 1
		else:
			idx1+=1
			idx2+=1
	return True

def isOneEditAway(s1,s2):
	if len(s1)==len(s2):
		return oneEditReplace(s1,s2)
	elif len(s1) == len(s2)+1:
		return oneEditInsert(s1,s2)
	elif len(s1)+1 == len(s2):
		return oneEditInsert(s2,s1)
	return False

s1 = "pale"
s2 = "bale"
print isOneEditAway(s1,s2)