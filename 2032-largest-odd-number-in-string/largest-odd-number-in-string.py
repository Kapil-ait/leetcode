"""class Solution(object):
    def largestOddNumber(self, num):
        result=[]
        for i in range(len(num)):
          for j in range(i+1, len(num)+1):
            result.append(num[i:j])
        r = ""
        for k in range(len(result)):
            if int(result[k][-1]) % 2 != 0:
                if len(result[k]) > len(r):
                    r = result[k]

        return r"""

class Solution(object):
    def largestOddNumber(self,num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""
        