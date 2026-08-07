class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        
        R2 = R3 = R5 = R7 = 0
        temp = t
        while temp % 2 == 0: R2 += 1; temp //= 2
        while temp % 3 == 0: R3 += 1; temp //= 3
        while temp % 5 == 0: R5 += 1; temp //= 5
        while temp % 7 == 0: R7 += 1; temp //= 7
        
        if temp > 1:
            return "-1"

        DIGIT_FACTORS = (
            (0, 0, 0, 0), 
            (0, 0, 0, 0), 
            (1, 0, 0, 0),
            (0, 1, 0, 0), 
            (2, 0, 0, 0),
            (0, 0, 1, 0), 
            (1, 1, 0, 0), 
            (0, 0, 0, 1), 
            (3, 0, 0, 0), 
            (0, 2, 0, 0), 
        )

        def get_len23(c2: int, c3: int) -> int:
            if c2 <= 0 and c3 <= 0:
                return 0
            c2 = max(0, c2); c3 = max(0, c3)
            c8, r2 = divmod(c2, 3)
            c9, r3 = divmod(c3, 2)
            extra_len = 2 if (r2 == 2 and r3 == 1) else (1 if (r2 or r3) else 0)
            return c8 + c9 + extra_len

        def get_digits23(c2: int, c3: int) -> str:
            if c2 <= 0 and c3 <= 0:
                return ""
            c2 = max(0, c2); c3 = max(0, c3)
            c8, r2 = divmod(c2, 3)
            c9, r3 = divmod(c3, 2)
            
            if r2 == 0 and r3 == 0: extra = ""
            elif r2 == 1 and r3 == 0: extra = "2"
            elif r2 == 2 and r3 == 0: extra = "4"
            elif r2 == 0 and r3 == 1: extra = "3"
            elif r2 == 1 and r3 == 1: extra = "6"
            else: extra = "26" 
                
            return extra + "8" * c8 + "9" * c9

        n = len(num)

        if '0' not in num:
            p2 = p3 = p5 = p7 = 0
            for char in num:
                v2, v3, v5, v7 = DIGIT_FACTORS[ord(char) - 48]
                p2 += v2; p3 += v3; p5 += v5; p7 += v7
            if p2 >= R2 and p3 >= R3 and p5 >= R5 and p7 >= R7:
                return num

        z = num.find('0')
        limit = n if z == -1 else z
        
        pref = [(0, 0, 0, 0)] * (n + 1)
        curr2 = curr3 = curr5 = curr7 = 0
        for i in range(limit):
            v2, v3, v5, v7 = DIGIT_FACTORS[ord(num[i]) - 48]
            curr2 += v2; curr3 += v3; curr5 += v5; curr7 += v7
            pref[i + 1] = (curr2, curr3, curr5, curr7)

        for i in range(min(n - 1, limit), -1, -1):
            p2, p3, p5, p7 = pref[i]
            rem2_before = R2 - p2
            rem3_before = R3 - p3
            rem5_before = R5 - p5
            rem7_before = R7 - p7

            L_base = max(0, rem5_before) + max(0, rem7_before) + get_len23(rem2_before, rem3_before)
            L = n - 1 - i  
            if L_base - 1 > L:
                continue

            start_d = ord(num[i]) - 48 + 1
            for d in range(start_d, 10):
                v2, v3, v5, v7 = DIGIT_FACTORS[d]
                rem2 = max(0, rem2_before - v2)
                rem3 = max(0, rem3_before - v3)
                rem5 = max(0, rem5_before - v5)
                rem7 = max(0, rem7_before - v7)

                req_len = rem5 + rem7 + get_len23(rem2, rem3)
                if req_len <= L:
                    seq23 = get_digits23(rem2, rem3)
                    seq_other = "".join(sorted(seq23 + "5" * rem5 + "7" * rem7))
                    pad1_count = L - req_len
                    suffix = "1" * pad1_count + seq_other
                    return num[:i] + str(d) + suffix

        req_full = max(0, R5) + max(0, R7) + get_len23(R2, R3)
        seq_full = get_digits23(R2, R3)
        seq_other = "".join(sorted(seq_full + "5" * max(0, R5) + "7" * max(0, R7)))
        target_len = max(n + 1, req_full)
        pad_count = target_len - len(seq_other)
        return "1" * pad_count + seq_other