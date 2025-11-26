class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def myPow(self, x: float, n: int) -> float:
        ans = 1;
        N = abs(n);
        while N > 0:
            if N & 1 == 1:
                ans = ans * x;
                N -= 1;
            else:
                x = x*x;
                N = N // 2;
        if n < 0:
            return 1 / ans;
        return ans;


        