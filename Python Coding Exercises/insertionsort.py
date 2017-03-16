a = [2,4,3,5,7,8]
x = 0
j = 0
#Insertion sort
for i in range(1,len(a)):
    x = a[i]
    j = i-1
    while j>=0 and a[j]>x:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = x

print a
    
