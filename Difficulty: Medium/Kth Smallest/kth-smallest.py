import heapq;
# Optimal Approach
# Time Complexity: O(nlogk)
# Space Complexity: O(1)
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        pq = [];
        for i in range(k):
            heapq.heappush(pq, -arr[i]);
        
        for j in range(k, len(arr)):
            if  arr[j] < -pq[0]:
                heapq.heappop(pq);
                heapq.heappush(pq, -arr[j]);
        return -pq[0];
