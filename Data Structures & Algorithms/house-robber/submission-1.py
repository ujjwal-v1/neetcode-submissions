class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        first, second = 0, nums[0]
        for i in range(1, n):
            third = max(second, nums[i]+first)
            first, second = second, third
            
        return second
        