class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        
        cnt = [0] * (M + 1)
        for v in nums:
            cnt[v] += 1
        
        cntMultiple = [0] * (M + 1)
        for g in range(1, M + 1):
            total = 0
            for multiple in range(g, M + 1, g):
                total += cnt[multiple]
            cntMultiple[g] = total
        
        pairs = [0] * (M + 1)
        for g in range(1, M + 1):
            c = cntMultiple[g]
            pairs[g] = c * (c - 1) // 2
        
        exact = pairs[:] 
        for g in range(M, 0, -1):
            k = 2 * g
            while k <= M:
                exact[g] -= exact[k]
                k += g
        
        prefix = [0] * (M + 1)
        for g in range(1, M + 1):
            prefix[g] = prefix[g - 1] + exact[g]
        
        answer = []
        for q in queries:
            g = bisect.bisect_right(prefix, q)
            answer.append(g)
        
        return answer