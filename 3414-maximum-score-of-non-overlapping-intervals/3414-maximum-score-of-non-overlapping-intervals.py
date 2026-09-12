from typing import List
from bisect import bisect_right


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        arr.sort()

        starts = [x[0] for x in arr]

        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        dp = [[None] * 5 for _ in range(n + 1)]

        def better(a, b):
            """
            Return the better of two:
            (score, tuple(indices))
            """
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        def solve(i, k):
            if i == n or k == 0:
                return (0, ())

            if dp[i][k] is not None:
                return dp[i][k]

            best = solve(i + 1, k)

            score, indices = solve(nxt[i], k - 1)

            candidate = (
                score + arr[i][2],
                tuple(sorted(indices + (arr[i][3],)))
            )

            best = better(best, candidate)

            dp[i][k] = best
            return best

        return list(solve(0, 4)[1])