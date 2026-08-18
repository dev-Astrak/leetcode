from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}
        n = len(nums)

        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x, freq in count.items():
            if freq == 1:
                ans = max(ans, x)

        return ans