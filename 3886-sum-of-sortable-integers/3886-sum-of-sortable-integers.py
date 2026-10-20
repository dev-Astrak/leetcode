class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            ok = True
            prev_max = None

            for i in range(0, n, k):
                block = nums[i:i + k]

                desc = 0
                for j in range(k - 1):
                    if block[j] > block[j + 1]:
                        desc += 1
                        if desc > 1:
                            break

                if desc <= 1 and k > 1 and block[-1] > block[0]:
                    desc += 1

                if desc > 1:
                    ok = False
                    break

                mn = min(block)
                mx = max(block)

                if prev_max is not None and prev_max > mn:
                    ok = False
                    break

                prev_max = mx

            if ok:
                ans += k

        return ans