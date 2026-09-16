class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        def comb(a, b, mod):
            if b < 0 or b > a:
                return 0
            b = min(b, a - b)
            num = 1
            den = 1
            for i in range(b):
                num = num * (a - i) % mod
                den = den * (i + 1) % mod
            return num * pow(den, mod - 2, mod) % mod
        
        return comb(n + k - 1, 2 * k, MOD)