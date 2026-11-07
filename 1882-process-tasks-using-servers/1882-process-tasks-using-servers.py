import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        busy = []
        heapq.heapify(available)

        ans = []
        time = 0

        for j, task in enumerate(tasks):
            time = max(time, j)

            while busy and busy[0][0] <= time:
                free_time, weight, i = heapq.heappop(busy)
                heapq.heappush(available, (weight, i))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, i = heapq.heappop(busy)
                    heapq.heappush(available, (weight, i))

            weight, i = heapq.heappop(available)
            ans.append(i)

            heapq.heappush(busy, (time + task, weight, i))

        return ans