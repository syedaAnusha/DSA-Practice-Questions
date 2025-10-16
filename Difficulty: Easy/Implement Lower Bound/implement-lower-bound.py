class Solution:
    # Brute Force Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def lowerBound(self, arr, target):
        # code here
        ind = len(arr);
        low = 0;
        high = ind - 1;
        while low <= high:
            mid = (low + high) // 2;
            if arr[mid] >= target:
                ind = mid;
                high = mid - 1;
            else:
                low = mid + 1;
        return ind;
            
            
        