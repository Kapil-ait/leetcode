class Solution(object):
    def numOfSubarrays(self, arr):
        odd = 0
        even = 1
        total = 0
        result = 0
        mod = 10**9 + 7

        for num in arr:
            total += num

            if total % 2 == 0:
                result += odd
                even += 1
            else:
                result += even
                odd += 1

        return result % mod