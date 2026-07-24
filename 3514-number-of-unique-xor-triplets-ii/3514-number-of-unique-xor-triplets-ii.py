from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n_bits = 11         
        full = 1 << n_bits 

        masks = []
        for b in range(n_bits):
            block = 1 << b
            m = 0
            for i in range(0, full, 2 * block):
                m |= ((1 << block) - 1) << i
            masks.append(m)

        def xorshift(x: int, a: int) -> int:
            for b in range(n_bits):
                if a & (1 << b):
                    block = 1 << b
                    m = masks[b]
                    x = ((x & m) << block) | ((x >> block) & m)
            return x

        S = set(nums)

        bitset = 0
        for v in S:
            bitset |= (1 << v)

        pair = 0
        for a in S:
            pair |= xorshift(bitset, a)

        final = 0
        for c in S:
            final |= xorshift(pair, c)

        return bin(final).count('1')