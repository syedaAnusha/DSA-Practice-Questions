class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, arr, x):
        # code here
        index = -1;
        for i in range(len(arr)):
            if arr[i] == x:
                return i;
        
        return -1;