class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # space optimized
        dp = [1]*n
        
        for i in range(1, m):
            tmp = [1]*n
            for j in range(1, n):
                tmp[j] = dp[j] + tmp[j-1]
            dp = tmp

        return dp[n-1]
        