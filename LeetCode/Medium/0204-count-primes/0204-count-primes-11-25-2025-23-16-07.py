class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n log(log n)) + O(n)
    # Space Complexity: O(n)
    def countPrimes(self, n: int) -> int:
        primeSet = [1 for _ in range(n+1)];
        i = 2; # smallest even prime
        totalPrimes = 0;
        while i*i <= n:
            if primeSet[i] == 1:
                j = i*i;
                while j <= n:
                    primeSet[j] = 0;
                    j += i;
            i += 1;
        
        for i in range(len(primeSet)-1):
            if i > 1 and primeSet[i] == 1:
                totalPrimes += 1;
        return totalPrimes;