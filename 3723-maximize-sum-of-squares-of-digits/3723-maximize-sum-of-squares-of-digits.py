class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        return "9" * (sum // 9) + str(sum % 9) * (1 if sum % 9 else 0) + "0" * (num - (sum // 9) - (1 if sum % 9 else 0))