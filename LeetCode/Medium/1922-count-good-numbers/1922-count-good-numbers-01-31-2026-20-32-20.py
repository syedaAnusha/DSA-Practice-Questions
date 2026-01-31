class Solution:
    # Optimal Approach - Iterative Approach
    # Time Complexity: O(2log n)
    # Space Complexity: O(1)
    MOD = 1_000_000_007;
    def myPow(self, x, n):
        ans = 1;
        x %= self.MOD;
        while n > 0:
            if n & 1:
                ans = (ans * x) % self.MOD;
            x = (x * x) % self.MOD;
            n >>= 1;
        return ans;

    def countGoodNumbers(self, n: int) -> int:
        countOfEvens = (n+1) // 2;
        countOfPrimes = n//2;
        
        evenNums = self.myPow(5, countOfEvens);
        primeNums = self.myPow(4, countOfPrimes);
        return (evenNums * primeNums) % self.MOD; 