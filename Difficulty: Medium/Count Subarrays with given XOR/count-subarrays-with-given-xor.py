class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def subarrayXor(self, arr, k):
        # code here
        totalXorCnt = 0;
        xor = 0;
        xorSet = dict();
        xorSet[xor] = 1;
        for i in range(len(arr)):
            xor = xor ^ arr[i];
            x = xor ^ k;
            if x in xorSet:
                totalXorCnt += xorSet[x];
            if xor in xorSet:
                xorSet[xor] += 1;
            else:
                xorSet[xor] = 1
            
        return totalXorCnt;