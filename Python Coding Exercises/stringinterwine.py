# String interwining

def interwine(s1,s2):
	newStr = []
	for i in range(min(len(s2),len(s1))):
		new = s1[i]+s2[i]
		newStr.append(new)
		
	if len(s2)>len(s1):
		newStr.append(s2[i+1:])
	else:
		newStr.append(s1[i+1:])
	print ("").join(newStr)
s1 = "para"
s2 = "nakhwaashhaslkdla"
interwine(s1,s2)
