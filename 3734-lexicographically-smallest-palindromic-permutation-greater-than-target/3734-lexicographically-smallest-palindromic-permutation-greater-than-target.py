class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd_chars = [i for i in range(26) if cnt[i] % 2 == 1]
        if n % 2 == 0:
            if len(odd_chars) != 0:
                return ""
            mid_char = None
        else:
            if len(odd_chars) != 1:
                return ""
            mid_char = chr(odd_chars[0] + 97)

        m = n // 2
        pool = [cnt[i] // 2 for i in range(26)]

        # find longest feasible matched prefix length (max_i) for target[0:m] from pool
        pool_states = [pool[:]]
        cur = pool[:]
        max_i = 0
        for i in range(m):
            c = ord(target[i]) - 97
            if cur[c] > 0:
                cur = cur[:]
                cur[c] -= 1
                pool_states.append(cur)
                max_i = i + 1
            else:
                break

        def build_sorted(p):
            return ''.join(chr(i + 97) * p[i] for i in range(26))

        # Candidate: full prefix match (longest possible), check if resulting palindrome beats target
        if max_i == m:
            Q = target[:m]
            P = Q + (mid_char if mid_char else "")
            full = P + Q[::-1]
            if full > target:
                return full

        limit = max_i if max_i < m else m - 1

        for i in range(limit, -1, -1):
            remaining = pool_states[i]
            tc = ord(target[i]) - 97
            chosen = -1
            for c in range(tc + 1, 26):
                if remaining[c] > 0:
                    chosen = c
                    break
            if chosen == -1:
                continue

            newpool = remaining[:]
            newpool[chosen] -= 1
            fill = build_sorted(newpool)
            Q = target[:i] + chr(chosen + 97) + fill
            P = Q + (mid_char if mid_char else "")
            full = P + Q[::-1]
            return full

        return ""