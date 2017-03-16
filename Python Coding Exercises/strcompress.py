#String compression in python
#ctci 1.6

def strcompress(s):
	count = 1
	newstr = []
	for i in range(len(s)-1):
		if s[i]==s[i+1]:
			count+=1
		else:
			newstr.append(s[i])
			newstr.append(str(count))
			count = 1
	if count>0:
		newstr.append(s[-1])
		newstr.append(str(count))
		
	if len(newstr)<len(s):
		return ("").join(newstr)
	else: 
		return s

s = "aaabbccaA"
print strcompress(s)