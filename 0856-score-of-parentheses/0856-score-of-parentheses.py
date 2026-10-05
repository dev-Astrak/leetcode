class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                current = stack.pop()

                if current == 0:
                    current = 1
                else:
                    current *= 2

                stack[-1] += current

        return stack[0]