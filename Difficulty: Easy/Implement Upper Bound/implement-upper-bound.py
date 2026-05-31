class Solution:
    # Optimal Approach
    # Time Complexity: O (log n)
    # Space Complexity: O(1)
    def upperBound(self, arr, target):
        # code here
        arrLen = len(arr);
        low = 0;
        high = arrLen - 1;
        index = arrLen;
        
        while low <= high:
            mid = (low + high) // 2;
            if arr[mid] > target:
                index = mid;
                high = mid - 1;
            else:
                low = mid + 1;
        
        return index;