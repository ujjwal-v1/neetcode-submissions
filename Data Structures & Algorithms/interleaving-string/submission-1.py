class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1)+1, len(s2)+1, len(s3)+1
        
        if n1+n2-1 != n3:
            return False 

        dp = [[False] * n2 for _ in range(n1)]

        dp[0][0] = True

        for i in range(n1):
            if i == 0: 
                continue
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]

        for j in range(n2):
            if j == 0: 
                continue
            dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]

        for i in range(1, n1):
            for j in range(1, n2):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        
        return dp[n1-1][n2-1]


        