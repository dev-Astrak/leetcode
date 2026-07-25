class Solution:
    def maxProduct(self, n: int) -> int:
        first = second = 0
        while n:
            d = n % 10
            n //= 10
            if d > first:
                first, second = d, first
            elif d > second:
                second = d
        return first * second