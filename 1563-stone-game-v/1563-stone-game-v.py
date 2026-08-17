from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]

        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        for i in range(n - 1, -1, -1):
            m = i

            for j in range(i + 1, n):
                total_sum = P[j + 1] - P[i]

                while m < j and (P[m + 1] - P[i]) * 2 < total_sum:
                    m += 1

                res = 0

                if m > i:
                    res = max(res, max_l[i][m - 1])

                if m < j:
                    if (P[m + 1] - P[i]) * 2 == total_sum:
                        res = max(res, max_l[i][m])
                        res = max(res, max_r[m + 1][j])
                    else:
                        res = max(res, max_r[m + 1][j])

                dp[i][j] = res
                max_l[i][j] = max(max_l[i][j - 1], total_sum + res)
                max_r[i][j] = max(max_r[i + 1][j], total_sum + res)

        return dp[0][n - 1]