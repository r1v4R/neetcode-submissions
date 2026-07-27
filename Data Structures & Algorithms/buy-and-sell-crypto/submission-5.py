class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        maxp=0
        for i in range(len(prices)):
            if prices[i]<prices[buy]:
                buy=i
            if prices[i]-prices[buy]>maxp:
                maxp=prices[i]-prices[buy]
        if maxp>=0:
            return maxp
        else:
            return 0