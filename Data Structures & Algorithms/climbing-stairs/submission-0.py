class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def solve(n):
            if n==1 or n==2:
                return n
            if n-1 in cache:
                n1=cache[n-1]
            else:
                n1 = solve(n-1)
            
            if n-2 in cache:
                n2 = cache[n-2]
            else:
                n2 = solve(n-2)

            cache[n] = n1+n2
            return cache[n]

        return solve(n)
        
        