import heapq
class Solution:
    def findAdjList(self, n, times):
        adj = [[]*n for _ in range(n)]
        for u, v, w in times:
            adj[u].append((v, w))

        return adj

    def findMinTime(self, adj, pq, timesArr, times):
        while pq:
            time, source = heapq.heappop(pq)
            for target, curTime in adj[source]:
                if curTime + time < timesArr[target]:
                    heapq.heappush(pq, (curTime + time, target))
                    timesArr[target] = curTime + time
        

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = self.findAdjList(n+1, times)
        pq = []
        timesArr = [float('inf')] * (n+1)
        timesArr[k] = 0
        heapq.heappush(pq, (0, k))
        self.findMinTime(adj, pq, timesArr, times)
        minTime = 0
        for i in range(1,len(timesArr)):
            if timesArr[i] == float('inf'):
                return -1
            minTime = max(minTime, timesArr[i])
        return minTime 