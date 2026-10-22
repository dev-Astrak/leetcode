class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        k = nums[0]
        if all(nums[i] == (k + i) % n for i in range(n)):
            a = 0 if k == 0 else min(n - k, k + 2)
        else:
            a = float('inf')

        k = (n - 1 - nums[0]) % n
        if all(nums[i] == (n - 1 - k - i) % n for i in range(n)):
            b = 1 + min(k, n - k)
        else:
            b = float('inf')

        ans = min(a, b)
        return -1 if ans == float('inf') else ans