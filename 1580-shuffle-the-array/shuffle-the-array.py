class Solution(object):
    def shuffle(self, nums, n):
        num=[]       
        for i in range(len(nums)//2):
            num.append(nums[i])
            num.append(nums[i+n])
        return num
        