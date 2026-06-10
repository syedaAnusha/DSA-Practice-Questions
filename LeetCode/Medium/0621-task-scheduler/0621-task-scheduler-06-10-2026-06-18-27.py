import heapq;
from collections import Counter;
# Optimal Approach
# Time Complexity: O(nlogk)
# Space Complexity: O(k)
class Solution:
    def findLeastInterval(self, tasks, n):
        frequency = Counter(tasks);
        maxHeap = [];
        maxCPUIntervals = 0;
        for count in frequency.values():
            heapq.heappush(maxHeap, -count);

        while maxHeap:
            temp = [];
            time = 0;
            cycle = n+1;
            while maxHeap and time < cycle:
                freq = heapq.heappop(maxHeap);
                freq += 1;
                if -freq > 0:
                    temp.append(freq);
                maxCPUIntervals += 1
                time += 1;
            j = 0;
            while temp and j < len(temp):
                heapq.heappush(maxHeap, temp[j]);
                j += 1;
            if maxHeap:
                maxCPUIntervals += cycle-time;

        return maxCPUIntervals;

    def leastInterval(self, tasks: List[str], n: int) -> int:
        return self.findLeastInterval(tasks, n);      