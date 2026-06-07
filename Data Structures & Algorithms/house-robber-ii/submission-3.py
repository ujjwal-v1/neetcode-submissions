class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def solve(numbers: List[int]):
            rob1, rob2 = 0, 0
            for i in range(len(numbers)):
                tmp = max(numbers[i]+rob1, rob2)
                rob1, rob2 = rob2, tmp

            return rob2

        return max(solve(nums[:-1]), solve(nums[1:]))
        