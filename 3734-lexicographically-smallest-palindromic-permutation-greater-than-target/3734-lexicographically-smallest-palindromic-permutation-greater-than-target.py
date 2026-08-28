class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        if sum(x & 1 for x in cnt) > 1:
            return ""

        half_cnt = [x // 2 for x in cnt]
        m = n // 2

        mid = ""
        if n & 1:
            for i in range(26):
                if cnt[i] & 1:
                    mid = chr(i + 97)
                    break

        def build(c):
            return ''.join(chr(i + 97) * c[i] for i in range(26))

        def make(left):
            return left + mid + left[::-1]

        prefix = target[:m]
        used = [0] * 26
        feasible = True

        for c in prefix:
            x = ord(c) - 97
            used[x] += 1
            if used[x] > half_cnt[x]:
                feasible = False
                break

        if feasible:
            left = prefix
            candidate = make(left)
            if candidate > target:
                return candidate

        for i in range(m - 1, -1, -1):
            used = [0] * 26
            ok = True

            for j in range(i):
                x = ord(target[j]) - 97
                used[x] += 1
                if used[x] > half_cnt[x]:
                    ok = False
                    break

            if not ok:
                continue

            cur = ord(target[i]) - 97

            for x in range(cur + 1, 26):
                if used[x] < half_cnt[x]:
                    used[x] += 1
                    remain = [
                        half_cnt[j] - used[j]
                        for j in range(26)
                    ]

                    left = target[:i] + chr(x + 97) + build(remain)
                    candidate = make(left)

                    if candidate > target:
                        return candidate

        return ""