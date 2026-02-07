#User function Template for python3
class Solution:
    # Brute Force Approach
    # Time Complexity: O(2^N)
    # Space Complexity: O(N)
    def isSubsequenceSum(self, arr, k, index):
        if k == 0:
            return True;
        if k < 0:
            return False;
        if index == len(arr):
            return k == 0;
        if self.isSubsequenceSum(arr, k-arr[index], index+1):
            return True;
        self.isSubsequenceSum(arr, k, index+1);
        
    def checkSubsequenceSum(self, N, arr, K):
        # Code here
        index = 0;
        subseqArr = [];
        return self.isSubsequenceSum(arr, K, index);
