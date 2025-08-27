class Solution:
# Brute Force Approach for array contain positive numbers only
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def longestSubarray(self, arr, k):
    # code here
    maxLen = 0;
    for i in range(len(arr)):
        Sum = 0;
        for j in range(i, len(arr)):
            Sum += arr[j];
            if Sum == k:
                maxLen = max(maxLen, j-i+1);
    return maxLen;
