class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        sm = [0] * size
        sq = [0] * size
        lazy = [0] * size

        def apply(node, l, r, v):
            length = r - l + 1
            sq[node] = (sq[node] + 2 * v * sm[node] + v * v * length) % MOD
            sm[node] = (sm[node] + v * length) % MOD
            lazy[node] += v

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return
            m = (l + r) // 2
            v = lazy[node]
            apply(node * 2, l, m, v)
            apply(node * 2 + 1, m + 1, r, v)
            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return
            push(node, l, r)
            m = (l + r) // 2
            if ql <= m:
                update(node * 2, l, m, ql, qr)
            if qr > m:
                update(node * 2 + 1, m + 1, r, ql, qr)
            sm[node] = (sm[node * 2] + sm[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, r)
            ans = (ans + sq[1]) % MOD
            last[x] = r

        return ans