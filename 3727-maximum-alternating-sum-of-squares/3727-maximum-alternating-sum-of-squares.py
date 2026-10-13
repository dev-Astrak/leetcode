class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x, reverse=True)
        return sum(x * x * (1 if i < (len(nums) + 1) // 2 else -1) for i, x in enumerate(nums))