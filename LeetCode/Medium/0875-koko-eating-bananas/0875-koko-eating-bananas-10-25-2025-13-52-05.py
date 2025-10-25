class Solution:
    # Optimal Approach
    # Time Complexity: O(log max(pile) * n), here n = length of piles
    # Space Complexity: O(1)
    def requiredTimeToEatBananas(self, piles, k):
        totalTime = 0;
        for i in range(len(piles)):
            totalTime += math.ceil(piles[i]/k);
        return totalTime;

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1;
        high = max(piles);

        while low <= high:
            mid = (low + high) // 2; # k number of bananas koko can eat
            if self.requiredTimeToEatBananas(piles, mid) <= h:
                high = mid - 1;
            else:
                low = mid + 1;
        return low;

