class Solution:
    # Optimal Approach
    # Time Complexity: O(n* log(sum - max + 1)
    # Space Complexity: O(1)
    def findNoOfStds(self, arr, pages):
        std = 1;
        allocatedPages = 0;
        for i in range(len(arr)):
            if arr[i] + allocatedPages <= pages:
                allocatedPages += arr[i];
            else:
                std += 1;
                allocatedPages = arr[i];
        return std;
                
    def findPages(self, arr, k):
        # code here
        low = max(arr);
        high = sum(arr);
        
        if len(arr) < k:
            return -1;
        
        while low <= high:
            mid = (low + high) // 2;
            noOfStudents = self.findNoOfStds(arr, mid);
            if noOfStudents <= k:
                high = mid - 1;
            else:
                low = mid + 1;
        return low;
            
