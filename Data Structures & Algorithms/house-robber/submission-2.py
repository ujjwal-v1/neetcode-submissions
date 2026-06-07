class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second, n = 0, 0, len(nums)

        for i in range(n):
            tmp = max(nums[i]+first, second)
            first, second = second, tmp
        
        return second
        