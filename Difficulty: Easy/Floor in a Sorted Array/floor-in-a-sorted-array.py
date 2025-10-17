class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findFloor(self, arr, x):
        # code here
        n = len(arr);
        low = 0;
        high = n - 1;
        index = -1;
        while low <= high:
            mid = (low + high) // 2;
            if arr[mid] > x:
                high = mid - 1;
            elif (arr[mid] <= x and arr[mid] >= arr[index]) or index == -1:
                index = mid;
                low = mid + 1;
            else:
                low = mid + 1;
                
        return index;
                
                
                
                
            
        