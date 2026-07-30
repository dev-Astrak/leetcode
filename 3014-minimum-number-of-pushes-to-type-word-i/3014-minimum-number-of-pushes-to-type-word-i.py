class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        q, r = divmod(n, 8)
        return 8 * q * (q + 1) // 2 + r * (q + 1)