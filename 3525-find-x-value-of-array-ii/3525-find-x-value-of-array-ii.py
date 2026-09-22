class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [(0, [0] * k) for _ in range(4 * n)]

        def make_node(value):
            p = value % k
            cnt = [0] * k
            cnt[p] = 1
            return p, cnt

        def merge(a, b):
            pa, ca = a
            pb, cb = b
            cnt = ca[:]

            for r in range(k):
                cnt[(pa * r) % k] += cb[r]

            return (pa * pb) % k, cnt

        def build(node, l, r):
            if l == r:
                tree[node] = make_node(nums[l])
                return

            m = (l + r) // 2
            build(node * 2, l, m)
            build(node * 2 + 1, m + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, value):
            if l == r:
                tree[node] = make_node(value)
                return

            m = (l + r) // 2

            if idx <= m:
                update(node * 2, l, m, idx, value)
            else:
                update(node * 2 + 1, m + 1, r, idx, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            m = (l + r) // 2

            if qr <= m:
                return query(node * 2, l, m, ql, qr)

            if ql > m:
                return query(node * 2 + 1, m + 1, r, ql, qr)

            return merge(
                query(node * 2, l, m, ql, qr),
                query(node * 2 + 1, m + 1, r, ql, qr)
            )

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            nums[index] = value
            update(1, 0, n - 1, index, value)
            _, cnt = query(1, 0, n - 1, start, n - 1)
            ans.append(cnt[x])

        return ans