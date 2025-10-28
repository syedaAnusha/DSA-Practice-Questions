class Solution:
    # Optimal Approach
    # Time Complexity: O(log (sum - max + 1)) * O(n)
    # Space Complexity: O(1)
    def allocateBoards(self, totalTime, arr):
        workers = 1;
        time = 0;

        for i in range(len(arr)):
            if  time + arr[i] <= totalTime:
                time += arr[i];
            else:
                workers += 1;
                time = arr[i];
        return workers;
        
    def minTime (self, arr, k):
        # code here
        low = max(arr);
        high = sum(arr);
        if k == 1:
            return high;
  
        if len(arr) < k:
            return -1;
        
        while low <= high:
            mid = (low + high) // 2;
            noOfWorkers = self.allocateBoards(mid, arr);
            if noOfWorkers <= k:
                high = mid - 1;
            else:
                low = mid + 1;
        return low;
    