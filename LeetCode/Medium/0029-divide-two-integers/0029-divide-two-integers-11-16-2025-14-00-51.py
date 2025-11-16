class Solution:
    # Optimal Approach
    # Time Complexity ≈ O(log n)^2
    # Space Complexity = O(1)
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True;
        if dividend == divisor:
            return 1;
        if dividend >= 0 and divisor < 0:
            sign = False;
        if dividend < 0 and divisor >= 0:
            sign = False;
        n = abs(dividend);
        d = abs(divisor);
        ans = 0;

        while n >= d:
            cnt = 0;
            while (d << (cnt + 1)) < n:
                cnt += 1;
            ans += (1 << cnt);
            n = n - (d << cnt);

        # when ans is strictly equal or greater to 2^31, we need to return 2^31-1
        # e.g 2^31 = 2147483648
        if ans >= (1<<31) and sign == True:
            return ans-1;
        if ans >= (1<<31) and sign == False:
            return -ans;
        if sign == False:
            return -ans;

        return ans;

        