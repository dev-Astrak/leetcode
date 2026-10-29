class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import deque

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p
                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, i, val):
                i += 1
                while i <= self.n:
                    self.bit[i] ^= val
                    i += i & -i

            def query(self, i):
                res = 0
                while i > 0:
                    res ^= self.bit[i]
                    i -= i & -i
                return res

            def range_query(self, l, r):
                return self.query(r) ^ self.query(l)

        chars = list(s)
        fw = Fenwick(n)

        for u in range(n):
            bit = 1 << (ord(chars[u]) - ord('a'))
            fw.add(tin[u], bit)
            fw.add(tout[u], bit)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_bit = 1 << (ord(chars[u]) - ord('a'))
                new_bit = 1 << (ord(c) - ord('a'))
                delta = old_bit ^ new_bit

                fw.add(tin[u], delta)
                fw.add(tout[u], delta)
                chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask_u = fw.range_query(tin[w], tin[u] + 1)
                mask_v = fw.range_query(tin[w], tin[v] + 1)
                mask = mask_u ^ mask_v ^ (1 << (ord(chars[w]) - ord('a')))

                ans.append((mask & (mask - 1)) == 0)

        return ans