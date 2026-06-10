class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold, sold, cool = [0]*n, [0]*n, [0]*n
        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i-1], cool[i-1]-prices[i])
            cool[i] = max(sold[i-1], cool[i-1])
            sold[i] = hold[i-1]+prices[i]
        
        return max(0, sold[n-1], cool[n-1])