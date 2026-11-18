class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result1=[]
        result2=[]
        for i in range(m):
            result1.append(nums1[i])
        for j in range(n):
            result2.append(nums2[j])
        nums1[:]=sorted(result1+result2)
        