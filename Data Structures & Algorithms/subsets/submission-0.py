class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, temp = [], []
        def backtrack(index, temp):
            if index == n:
                ans.append(temp[:])
                return

            backtrack(index+1, temp)
            temp.append(nums[index])
            backtrack(index+1, temp)
            temp.pop()

        backtrack(0, temp)
        return ans
        