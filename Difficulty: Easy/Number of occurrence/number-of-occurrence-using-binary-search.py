class Solution:
    # Optimal Approach
    # Time Complexity: O(2 log n)
    # Space Complexity: O(1)
    def firstOccurence(self, arr, target):
        n = len(arr);
        low = 0;
        high = n - 1;
        firstIndex = -1;

        while low <= high:
            mid = (low + high) // 2;
            if arr[mid] == target:
                firstIndex = mid;
                high = mid - 1;
            elif arr[mid] > target:
                high = mid - 1;
            else:
                low = mid + 1;
        
        return firstIndex;
        
    def lastOccurence(self, arr, target):
        n = len(arr);
        low = 0;
        high = n - 1;
        lastIndex = -1;

        while low <= high:
            mid = (low + high) // 2;
            if arr[mid] == target:
                lastIndex = mid;
                low = mid + 1;
            elif arr[mid] > target:
                high = mid - 1;
            else:
                low = mid + 1;
        
        return lastIndex;
                
                
            
    def countFreq(self, arr, target):
        # code here
        firstPosition = self.firstOccurence(arr, target);
        if firstPosition == -1:
            return 0;
            
        lastPosition = self.lastOccurence(arr, target);
        cnt = (lastPosition - firstPosition) + 1;
        return cnt;
