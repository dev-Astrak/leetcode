class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        c = [0] * 26
        for ch in s:
            c[ord(ch) - 97] += 1

        snapshots = [c[:]]
        cur = c[:]
        matched = 0
        for i in range(n):
            t = ord(target[i]) - 97
            if cur[t] > 0:
                cur[t] -= 1
                matched += 1
                snapshots.append(cur[:])
            else:
                break

        maxI = min(matched, n - 1)
        for i in range(maxI, -1, -1):
            rem = snapshots[i]
            t = ord(target[i]) - 97
            found = -1
            for ch in range(t + 1, 26):
                if rem[ch] > 0:
                    found = ch
                    break
            if found != -1:
                prefix = target[:i]
                rem2 = rem[:]
                rem2[found] -= 1
                suffix_parts = []
                for ch in range(26):
                    if rem2[ch] > 0:
                        suffix_parts.append(chr(ch + 97) * rem2[ch])
                return prefix + chr(found + 97) + ''.join(suffix_parts)

        return ""