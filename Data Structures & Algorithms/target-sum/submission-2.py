class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        for num in nums:
            total+=num
        
        # sumP - sumN = target
        # sumP + sumN = total

        sumP = (total+target)/2

        if target > total or (total+target)%2 != 0:
            return 0
        
        dp = [0] * (int(sumP)+1)

        dp[0] = 1
        
        for num in nums:
            for i in range(int(sumP), -1, -1):
                if i-num>=0:
                    dp[i] += dp[i-num]
        
        return dp[int(sumP)]
        