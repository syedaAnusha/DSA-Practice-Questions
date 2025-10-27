class Solution:
    # Optimal Approach
    # Time Complexity: O(n * log n)
    # Space Complexity: O(1)
    def canWePlace(self, stalls, cows, dist):
        countCows = 1;
        last = stalls[0];
        
        for i in range(len(stalls)):
            if stalls[i] - last >= dist:
                countCows += 1;
                last = stalls[i];
            if countCows == cows:
                return True;
        return False;
        
    def aggressiveCows(self, stalls, k):
        # code here
        stalls.sort();
        n = len(stalls);
        low = 1;
        high = stalls[n-1];
        while low <= high:
            mid = (low + high) // 2;
            canWePlaceCows = self.canWePlace(stalls, k, mid);
            if canWePlaceCows:
                low = mid + 1;
            else:
                high = mid - 1;
        return high;
    
        
        