class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        length = m + n - 1

        if length % 2:
            return False
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        mask = (1 << (length // 2 + 1)) - 1

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    cur = 1
                else:
                    cur = 0
                    if i:
                        cur |= dp[i - 1][j]
                    if j:
                        cur |= dp[i][j - 1]

                if grid[i][j] == '(':
                    cur = (cur << 1) & mask
                else:
                    cur >>= 1
                dp[i][j] = cur

        return bool(dp[-1][-1] & 1)