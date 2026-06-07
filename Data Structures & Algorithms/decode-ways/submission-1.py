class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        first = 1
        second = 0 if s[0] == '0' else 1

        for i in range(2, n+1):
            tmp = 0
            if s[i-1] != '0':
                tmp+=second
            if 10 <= int(s[i-2:i]) <= 26:
                tmp+=first
            first, second = second, tmp
        
        return second



# 121326
# [1, 1, 2, 3]
        