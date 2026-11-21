class Solution(object):
    def findNumbers(self, nums):
        total=0
        for i in nums:
            count=0
            while i>0:
                count+=1
                i//=10
            if count%2==0:
                total+=1
        return total