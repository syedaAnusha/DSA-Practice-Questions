class Solution:
    # Optimal Approach using recursion
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    # Aux Space Complexity: O(log n) for recursive calls
    def findPower(self, x, n, ans):
        if n == 0:
            return ans;
        if n & 1 == 1:
            return self.findPower(x, n-1, ans*x);
        else:
            return self.findPower(x*x, n//2, ans);
        
    def myPow(self, x: float, n: int) -> float:
        ans = 1;
        N = abs(n);
        res = self.findPower(x, N, ans);
        if n < 0:
            return 1 / res;
        return res;