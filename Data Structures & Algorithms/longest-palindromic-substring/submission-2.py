class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        ans = ""
        maxLen = 0
        # odd len
        for i in range(n):
            left, right = i, i
            while left>=0 and right<n and s[left]==s[right]:
                strLen = right-left+1
                if maxLen<strLen:
                    maxLen = strLen
                    ans = s[left:right+1]
                left-=1
                right+=1
        
        # even length
        for i in range(n-1):
            left, right = i, i+1
            while left>=0 and right<n and s[left]==s[right]:
                strLen = right-left+1
                if maxLen<strLen:
                    maxLen = strLen
                    ans = s[left:right+1]
                left-=1
                right+=1
        
        return ans