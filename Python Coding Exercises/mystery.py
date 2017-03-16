def mystery(n):
    if n < 3:
        print "Hello"
    else:
        mystery(n-2)
        print "Hello"
        print "world"
        for i in range(9):
            print "world"

mystery(2)
