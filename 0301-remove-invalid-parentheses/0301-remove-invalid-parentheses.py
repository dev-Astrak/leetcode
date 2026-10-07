class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def remove(s, last_i, last_j, par):
            result = []
            balance = 0

            for i in range(last_i, len(s)):
                if s[i] == par[0]:
                    balance += 1
                elif s[i] == par[1]:
                    balance -= 1

                if balance >= 0:
                    continue

                for j in range(last_j, i + 1):
                    if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                        result.extend(
                            remove(
                                s[:j] + s[j + 1:],
                                i,
                                j,
                                par
                            )
                        )

                return result

            reversed_s = s[::-1]

            if par[0] == '(':
                return remove(reversed_s, 0, 0, (')', '('))

            return [reversed_s]

        return remove(s, 0, 0, ('(', ')'))