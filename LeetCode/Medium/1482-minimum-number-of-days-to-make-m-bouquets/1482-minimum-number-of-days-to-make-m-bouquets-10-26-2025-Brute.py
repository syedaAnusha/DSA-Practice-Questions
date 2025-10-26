class Solution:
    # Brute Force Approach
    # Time Complexity: O(n * O(max(n)-min(n)+1))
    # Space Complexity: O(1)
    def safeToPick(self, day, m, k, bloomDay):
        noOfBouquet = 0;
        totalPickedFlowers = 0;
        bloomDays = len(bloomDay);
        for i in range(bloomDays):
            if bloomDay[i] <= day:
                totalPickedFlowers += 1;
            else:
                noOfBouquet += totalPickedFlowers // k;
                totalPickedFlowers = 0;

        noOfBouquet += totalPickedFlowers // k;
        if noOfBouquet >= m:
            print(noOfBouquet);
            return True;
        else: 
            return False;

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        totalFlowers = m * k;
        n = len(bloomDay);
        minDays = min(bloomDay);
        maxDays = max(bloomDay);
        if totalFlowers > n:
            return -1; 
        for i in range(minDays, maxDays+1):
            if self.safeToPick(i, m, k, bloomDay):
                return i;
