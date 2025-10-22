class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findKRotation(self, arr):
        # code here
        low = 0;
        high = len(arr) - 1;
        minValue = float('inf');
        index = -1;
        
        while low <= high:
            mid = (low + high) // 2;
            if arr[low] <= arr[high]:
                if arr[low] < minValue:
                    index = low;
                    minValue = arr[low];
                return index;
            
            if arr[low] <= arr[mid]:
                if arr[low] < minValue:
                    minValue = arr[low];
                    index = low;
                low = mid + 1;
            
            else:
                if arr[mid] <= arr[high]:
                    if arr[mid] < minValue:
                        minValue = arr[mid];
                        index = mid;
                    high = mid - 1;
        return index;
                
                
                
        