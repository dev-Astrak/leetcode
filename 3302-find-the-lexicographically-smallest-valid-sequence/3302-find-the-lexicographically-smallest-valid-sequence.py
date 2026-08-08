from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        suf = [-1] * (m + 1)
        suf[m] = n  
        
        jj = m - 1
        for i in range(n - 1, -1, -1):
            if jj >= 0 and word1[i] == word2[jj]:
                suf[jj] = i
                jj -= 1

        
        res = []
        i = 0
        jj = 0
        used_mismatch = False
        
        while jj < m:
            if i >= n:
                return []
            
            if word1[i] == word2[jj]:
                res.append(i)
                i += 1
                jj += 1
            else:
                if not used_mismatch and suf[jj + 1] != -1 and i + 1 <= suf[jj + 1]:
                    res.append(i)
                    used_mismatch = True
                    i += 1
                    jj += 1
                else:
                    i += 1
        
        return res