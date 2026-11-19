class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        a = s1.split()
        b = s2.split()
        result=[]
        for i in range(len(a)):
              if a[i] not in b and a.count(a[i])==1:
                result.append(a[i])
        for j in range(len(b)):
            if b[j] not in a and b.count(b[j])==1:
                result.append(b[j])
        return result