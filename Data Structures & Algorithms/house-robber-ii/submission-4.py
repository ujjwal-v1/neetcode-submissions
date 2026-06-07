class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(numbers: List[int]):
            rob1, rob2 = 0, 0
            for i in numbers:
                tmp = max(i+rob1, rob2)
                rob1, rob2 = rob2, tmp

            return rob2

        return max(nums[0], solve(nums[:-1]), solve(nums[1:]))
        