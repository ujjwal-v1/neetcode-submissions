class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        for coin in coins:
            if coin<=amount:
                dp[coin] = 1
        
        for coin in coins:
            for money in range(amount+1):
                if money-coin >= 0 and dp[money-coin] != -1:
                    if dp[money] == -1:
                        dp[money] = dp[money-coin]+1
                    else:
                        dp[money] = min(dp[money-coin]+1, dp[money])
        
        return dp[amount]

        