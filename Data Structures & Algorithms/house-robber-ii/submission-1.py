class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        def solve(start, end):
            first, second = 0, nums[start]
            for i in range(start+1, end):
                third = max(nums[i]+first, second)
                first, second = second, third
            return second
        return max(solve(0, n-1), solve(1, n))
        