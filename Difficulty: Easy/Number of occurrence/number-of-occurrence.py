class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def countFreq(self, arr, target):
        # code here
        cnt = 0;
        for i in range(len(arr)):
            if arr[i] == target:
                cnt += 1;
        return cnt;
        