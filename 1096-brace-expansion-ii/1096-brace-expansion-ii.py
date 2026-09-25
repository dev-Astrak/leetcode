class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        i = 0

        def merge(a, b):
            return {x + y for x in a for y in b}

        def parse_expr():
            nonlocal i

            result = parse_term()

            while i < n and expression[i] == ',':
                i += 1
                result |= parse_term()

            return result

        def parse_term():
            nonlocal i

            result = {""}

            while i < n and expression[i] not in "},":
                if expression[i] == "{":
                    i += 1
                    part = parse_expr()
                    i += 1
                else:
                    part = {expression[i]}
                    i += 1

                result = merge(result, part)

            return result

        return sorted(parse_expr())