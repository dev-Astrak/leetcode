class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        middle = ""
        half = [0] * 26

        for i in range(26):
            if cnt[i] % 2:
                middle = chr(ord('a') + i)
            half[i] = cnt[i] // 2

        def ways(counts, total):
            res = 1
            used = 0

            for c in counts:
                if c == 0:
                    continue

                choose = 1
                for j in range(1, c + 1):
                    choose = choose * (used + j) // j
                    if choose >= k:
                        choose = k
                        break

                res *= choose
                if res >= k:
                    return k

                used += c

            return res

        if ways(half, half_len) < k:
            return ""

        ans = []

        for pos in range(half_len):
            remaining = half_len - pos - 1

            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                w = ways(half, remaining)

                if k > w:
                    k -= w
                    half[c] += 1
                else:
                    ans.append(chr(ord('a') + c))
                    break

        left = "".join(ans)
        return left + middle + left[::-1]