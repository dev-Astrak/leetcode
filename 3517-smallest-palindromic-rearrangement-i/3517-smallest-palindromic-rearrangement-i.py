class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        half = []
        mid = ''
        for c in sorted(cnt):
            c_half = cnt[c] // 2
            half.append(c * c_half)
            if cnt[c] % 2 == 1:
                mid = c
        half_str = ''.join(half)
        return half_str + mid + half_str[::-1]