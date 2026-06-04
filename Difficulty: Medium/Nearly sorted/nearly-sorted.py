import heapq;
# Optimal Approach
# Time Complexity: O(n log k)
# Space Complexity: O(k)
class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        index = 0;
        pq = [];
        
        for i in range(min(k+1, len(arr))):
            heapq.heappush(pq, arr[i]);
            
        for j in range(k+1, len(arr)):
            arr[index] = heapq.heappop(pq);
            heapq.heappush(pq, arr[j]);
            index += 1;
        
        while pq:
            arr[index] = heapq.heappop(pq);
            index += 1;
        return arr;