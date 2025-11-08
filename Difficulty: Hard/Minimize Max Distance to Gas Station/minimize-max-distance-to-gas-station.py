class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n * log (max_distance));
    # Space Complexity: O(1)
    def countNumOfGasStations(self, stations, distance):
        cnt = 0;
        n = len(stations);
        for i in range(1, n):
            gap = stations[i] - stations[i-1]
            cnt += int(gap / distance)  # Use normal division, not floor division
            
            #possibleGasStations = int((stations[i] - stations[i-1]) / distance);
            #if ((stations[i] - stations[i-1]) / distance) == (possibleGasStations * distance):
            #    possibleGasStations -= 1;
            #else:
            #    cnt += possibleGasStations;
        return cnt;
        
    def minMaxDist(self, stations, k):
        # Code here
        n = len(stations);
        low = 0;
        high = 0;
        for i in range(1, n):
            distance = stations[i] - stations[i-1];
            high = max(high, distance);
        
        diff = 1e-6;
        while high - low  > diff:
            mid = (low + high) / 2;
            cnt = self.countNumOfGasStations(stations, mid);
            if cnt > k:
                low = mid;
            else:
                high = mid;
        return high;
