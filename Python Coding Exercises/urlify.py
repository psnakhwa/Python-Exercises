# urlify in python
#ctci 1.3

def urlify(s,length):
	return s[:length].replace(" ","%20")

s = "Mr John Smith"
print urlify(s,len(s))