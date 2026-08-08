from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        occ = [[] for _ in range(26)]

        for i, ch in enumerate(word1):
            occ[ord(ch) - ord('a')].append(i)

        exact = [-1] * (m + 1)
        exact[m] = n

        pos = n - 1

        for j in range(m - 1, -1, -1):
            arr = occ[ord(word2[j]) - ord('a')]
            k = bisect_right(arr, pos) - 1

            if k < 0:
                break

            pos = arr[k]
            exact[j] = pos
            pos -= 1

        almost = [-1] * (m + 1)
        almost[m] = n

        for j in range(m - 1, -1, -1):
            limit = almost[j + 1]
            arr = occ[ord(word2[j]) - ord('a')]

            k = bisect_left(arr, limit) - 1
            match_position = arr[k] if k >= 0 else -1

            mismatch_position = limit - 1

            almost[j] = max(match_position, mismatch_position)

        next_diff = [[n] * 26 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            next_diff[i] = next_diff[i + 1].copy()
            current = ord(word1[i]) - ord('a')

            for c in range(26):
                if c != current:
                    next_diff[i][c] = i

        ans = []
        pos = 0
        mismatch_used = False

        for j in range(m):
            if pos >= n:
                return []

            target = word2[j]
            c = ord(target) - ord('a')

            if mismatch_used:
                arr = occ[c]
                k = bisect_left(arr, pos)

                if k == len(arr):
                    return []

                q = arr[k]

                if q + 1 > exact[j + 1]:
                    return []

            else:
                if word1[pos] == target:
                    if pos + 1 <= almost[j + 1]:
                        q = pos
                    else:
                        q = -1
                else:
                    if pos + 1 <= exact[j + 1]:
                        q = pos
                    else:
                        q = -1

                if q == -1:
                    arr = occ[c]
                    k = bisect_left(arr, pos)

                    if k < len(arr) and arr[k] + 1 <= almost[j + 1]:
                        q1 = arr[k]
                    else:
                        q1 = n

                    q2 = next_diff[pos][c]

                    if q2 < n and q2 + 1 <= exact[j + 1]:
                        pass
                    else:
                        q2 = n

                    q = min(q1, q2)

                    if q == n:
                        return []

            ans.append(q)

            if word1[q] != target:
                mismatch_used = True

            pos = q + 1

        return ans