"""class Solution(object):
    def maxProfit(self, prices):
        prev=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>prev:
                    result=prices[j]-prices[i]
                    prev=result
        return prev"""
class Solution(object):
    def maxProfit(self, prices):
        prev=0
        min_price=prices[0]
        for i in range(1, len(prices)):
            profit=prices[i]-min_price
            if profit>prev:
                prev=profit
            if prices[i]<min_price:
                min_price=prices[i]
        return prev
        