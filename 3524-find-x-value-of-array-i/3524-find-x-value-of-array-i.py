class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            r = num % k
            ndp = [0] * k
            ndp[r] += 1

            for x in range(k):
                ndp[(x * r) % k] += dp[x]

            dp = ndp

            for x in range(k):
                ans[x] += dp[x]

        return ans