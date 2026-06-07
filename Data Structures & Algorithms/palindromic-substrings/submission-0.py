class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0
        # odd len
        for i in range(n):
            left, right = i, i
            while left>=0 and right<n and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        
        # even length
        for i in range(n-1):
            left, right = i, i+1
            while left>=0 and right<n and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        
        return count
        