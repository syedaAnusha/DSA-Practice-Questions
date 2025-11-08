import heapq
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n * log n) + O(k * log n);
    # Space Complexity: O(n-1), where n = length of station
    def minMaxDist(self, stations, k):
        # Code here
        n = len(stations);
        howMany = [0 for _ in range(n)];
        pq = [];
        
        if len(stations) <= 1:
            return 0.00;
            
        for i in range(n-1):
            diff = (stations[i+1] - stations[i]);
            heapq.heappush(pq, (-diff, i))
        
        for gasStation in range(1,k+1):
            Distance, index = heapq.heappop(pq);
            howMany[index] += 1;
            original_gap = stations[index+1] - stations[index]
            sectionLength = original_gap / (howMany[index] + 1);
            heapq.heappush(pq, (-sectionLength, index))
            
        return -pq[0][0]; 
