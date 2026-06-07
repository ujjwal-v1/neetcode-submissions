class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        first = 1
        second = 0 if s[0]=='0' else 1

        for i in range(1, n):
            tmp = 0
            if s[i]!='0':
                tmp += second
            if 10 <= int(s[i-1:i+1]) <= 26:
                tmp += first
            first, second = second, tmp
        
        return second
        