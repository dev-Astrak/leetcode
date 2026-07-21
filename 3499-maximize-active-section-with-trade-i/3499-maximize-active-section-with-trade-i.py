class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        
        # Build run-length groups: list of (char, length)
        groups = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            groups.append((t[i], j - i))
            i = j
        
        total_ones = s.count('1')
        
        best_gain = 0
        k = len(groups)
        # Internal '1' groups are at even indices strictly between 0 and k-1
        # (groups alternate starting and ending with '1')
        for idx in range(2, k - 2, 2):
            # groups[idx] is a '1' block bounded by '0' blocks at idx-1 and idx+1
            left_zeros = groups[idx - 1][1]
            right_zeros = groups[idx + 1][1]
            gain = left_zeros + right_zeros
            best_gain = max(best_gain, gain)
        
        return total_ones + best_gain