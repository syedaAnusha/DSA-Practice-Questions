class Solution:
    # Optimal Solution
    # Time Complexity: O(N * log(sum - max + 1)
    # Space Complexity: O(1)
    def possibleToShip(self, weights, capacity):
        n = len(weights);
        days = 1;
        load = 0;
        for i in range(n):
            if (load + weights[i]) > capacity:
                days += 1;
                load = weights[i];
            else:
                load += weights[i];
        return days;

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights);
        high = sum(weights);

        while low <= high:
            mid = (low + high) // 2;
            minDaysRequired = self.possibleToShip(weights, mid); 
            if minDaysRequired <= days:
                high = mid - 1;
            else:
                low = mid + 1;

        return low;
        