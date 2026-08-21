from typing import List
from math import gcd


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # Precompute (LCM, sign) for every subset.
        subsets = []

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0
            valid = True

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    g = gcd(lcm, coins[i])
                    lcm = lcm // g * coins[i]

                    # LCM larger than the possible search range
                    # doesn't contribute for practical x.
                    if lcm > 10**18:
                        valid = False
                        break

            if valid:
                sign = 1 if bits % 2 == 1 else -1
                subsets.append((lcm, sign))

        def count(x: int) -> int:
            """Number of distinct achievable amounts <= x."""
            total = 0

            for lcm, sign in subsets:
                total += sign * (x // lcm)

            return total

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo