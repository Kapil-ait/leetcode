class Solution(object):
    def runningSum(self, nums):
        i=0
        c=nums[:]
        while i<len(nums):
            nums[i]=sum(c[:i+1])
            i+=1
        return nums
        