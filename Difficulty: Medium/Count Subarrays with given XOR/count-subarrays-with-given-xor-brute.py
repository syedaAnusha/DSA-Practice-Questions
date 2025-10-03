class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def subarrayXor(self, arr, k):
        # code here
        totalXorCnt = 0;
        for i in range(len(arr)):
            xor = 0;
            for j in range(i, len(arr)):
                xor = xor ^ arr[j];
                if xor == k:
                    totalXorCnt += 1;
        return totalXorCnt;
