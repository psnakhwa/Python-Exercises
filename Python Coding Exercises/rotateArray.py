class rotateArray:
    def rotate(nums,k):
        a=[0]*len(nums)
        for i in range(0,len(nums)
            a[i]=nums[(i+k)%len(nums)]

        return a

    n=[1,2,3,4,5,6,7]
    k=3
    z=rotate(n,k)
    print z
                     
     
