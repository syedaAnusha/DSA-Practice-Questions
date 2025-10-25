class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def floorSqrt(self, n): 
        # code here
        low = 1;
        high = n;
        ans = 1;
        while low <= high:
            mid = (low + high) // 2;
            val = (mid * mid);
            if val <= n:
                ans = mid;
                low = mid + 1;
            else:
                high = mid - 1;
                
        return ans;
        