class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s)+1, len(t)+1
        dp = [0] * n 
        dp[0] = 1

        for i in range(1, m):
            tmp = [0] * n
            for j in range(n):
                if j==0:
                    tmp[j] = 1
                    continue
                
                if s[i-1]==t[j-1]:
                    tmp[j] = dp[j-1] + dp[j]
                else:
                    tmp[j] = dp[j]
            dp = tmp
        
        return dp[-1]
