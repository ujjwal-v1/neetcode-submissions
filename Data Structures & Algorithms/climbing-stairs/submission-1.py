class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def solve(n):
            if n <=2:
                return n
            if n in cache:
                return cache[n]

            cache[n] = solve(n-1)+solve(n-2)
            return cache[n]

        return solve(n)
        
        