class Solution(object):
    def twoSum(self, nums, target):
        for i in range (0,len(nums)):
            for j in range (i+1, len(nums)):
                if nums[j]==target-nums[i]:
                    print i,j
sol =Solution()
sol.twoSum([2,3,7,9],11)
