class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        return sum(all(abs(x - y) > d for y in arr2) for x in arr1)