class Solution:
    # Optimal Appproach
    # Time Complexity: O(n) + O(n) = O(2n) = O(n)
    # Space Complexity: O(1)
    def twoOddNum(self, arr):
        #code here 
        b1 = 0;
        b2 = 0;
        xor = 0;
        for i in range(len(arr)):
            xor = xor ^ arr[i];
        
        rightMost = (xor & (xor -1)) ^ xor;
        for i in range(len(arr)):
            if arr[i] & rightMost:
                b1 = b1 ^ arr[i];
            else:
                b2 = b2 ^ arr[i];
        if b1 > b2:
            return [b1, b2];
        return [b2, b1];
