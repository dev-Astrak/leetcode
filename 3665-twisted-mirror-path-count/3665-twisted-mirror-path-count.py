class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    tot = 1
                elif grid[i][j] == 0:
                    tot = (R[i][j] + D[i][j]) % MOD
                else:
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + R[i][j]) % MOD
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + D[i][j]) % MOD
                    continue
                if i == m - 1 and j == n - 1:
                    ans = tot
                    continue
                if j + 1 < n:
                    R[i][j + 1] = (R[i][j + 1] + tot) % MOD
                if i + 1 < m:
                    D[i + 1][j] = (D[i + 1][j] + tot) % MOD
        return ans % MOD