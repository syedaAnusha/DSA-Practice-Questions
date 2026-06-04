#User function Template for python3
import heapq;
class Solution:
    # Optimal Approach
    # Time Complexity: O(n log n)
    # Space  Complexity: O(n) + O(n) 
    def replaceWithRank(self, N, arr):
        # Code here
        ranks = [0] * N;
        lastNum = 0;
        pq = [];
        rank = 0;
        
        for i in range(N):
            heapq.heappush(pq, (arr[i], i));
        
        while pq:
            num, numIndex = heapq.heappop(pq);
            if num != lastNum:
                rank += 1;
            ranks[numIndex] = rank;
            lastNum = num;
        return ranks;