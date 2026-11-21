class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        for i in range(len(candies)):
            r=candies[i]+extraCandies
            result.append(r)
        a=max(candies)
        f=[]
        for i in range(len(result)):
            if result[i]<a:
                f.append(False)
            else:
                f.append(True)
        return f

        