class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second, n = 0, 0, len(cost)

        for i in range(2, n+1):
            tmp = min(cost[i-2]+first, cost[i-1]+second)
            first, second = second, tmp
        
        return second
            
        