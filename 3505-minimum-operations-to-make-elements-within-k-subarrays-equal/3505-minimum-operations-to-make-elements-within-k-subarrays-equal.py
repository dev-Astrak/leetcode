import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        m = n - x + 1
        cost = [0] * m

        low = []   # max-heap (negated values)
        high = []  # min-heap
        delayed = defaultdict(int)
        low_size = high_size = 0
        low_sum = high_sum = 0

        def prune(heap, is_low):
            while heap:
                v = -heap[0] if is_low else heap[0]
                if delayed[v] > 0:
                    delayed[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal low_size, high_size, low_sum, high_sum
            if low_size > high_size + 1:
                v = -heapq.heappop(low)
                low_size -= 1
                low_sum -= v
                heapq.heappush(high, v)
                high_size += 1
                high_sum += v
                prune(low, True)
            elif low_size < high_size:
                v = heapq.heappop(high)
                high_size -= 1
                high_sum -= v
                heapq.heappush(low, -v)
                low_size += 1
                low_sum += v
                prune(high, False)

        def add(v):
            nonlocal low_size, high_size, low_sum, high_sum
            if not low or v <= -low[0]:
                heapq.heappush(low, -v)
                low_size += 1
                low_sum += v
            else:
                heapq.heappush(high, v)
                high_size += 1
                high_sum += v
            rebalance()

        def remove(v):
            nonlocal low_size, high_size, low_sum, high_sum
            delayed[v] += 1
            if low and v <= -low[0]:
                low_size -= 1
                low_sum -= v
                if v == -low[0]:
                    prune(low, True)
            else:
                high_size -= 1
                high_sum -= v
                if high and v == high[0]:
                    prune(high, False)
            rebalance()

        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                med = -low[0]
                cost[i - x + 1] = (med * low_size - low_sum) + (high_sum - med * high_size)

        INF = float('inf')
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and prev[i - x] != INF:
                    cand = prev[i - x] + cost[i - x]
                    if cand < cur[i]:
                        cur[i] = cand
            prev = cur
        return prev[n]