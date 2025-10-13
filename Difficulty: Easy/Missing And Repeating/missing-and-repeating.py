class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findTwoElement(self, arr):
        # code here
        # S - Sn = x - y
        # S2 - S2n = x + y
        n = len(arr);
        Sn = (n * (n + 1)) // 2;
        S2n = (n * (n + 1) * (2*n +1)) // 6; 
        S = 0;
        S2 = 0;
        for i in range(n):
            S += arr[i];
            S2 += arr[i] * arr[i];
        
        val1 = S - Sn; # x - y
        val2 = S2 - S2n;
        val2 = val2 // val1; # x + y
        x = (val1 + val2) // 2; 
        y = x - val1;
        
        return [x, y];
        
        
