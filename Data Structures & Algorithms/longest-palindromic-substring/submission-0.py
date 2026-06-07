class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = ""
        for i in range(n):
            dp[i][i] = True
            if len(ans)<1:
                ans = s[i]

            if i+1<n and s[i]==s[i+1]:
                dp[i][i+1]=True
                if len(ans)<2:
                    ans = s[i:i+2]

        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
                if dp[i][j] and len(ans)<j-i+1:
                    ans = s[i:j+1]
                    
        return ans
        