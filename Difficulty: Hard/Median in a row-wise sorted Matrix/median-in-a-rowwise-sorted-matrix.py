class Solution:
    # Optimal Approach
    # Time Complexity: O(log 10^9) * O(n * log m)
    # Space Complexity: O(1)
    def findUpperBound(self, arr, x):
        low = 0;
        high = len(arr)-1;
        
        while low <= high:
            mid = (low + high) // 2;
            if arr[mid] > x:
                high = mid - 1;
            else:
                low = mid + 1;
        return low;
        
    def countSmallerRequired(self, mat, mid):
        cnt = 0;
        for i in range(len(mat)):
            cnt += self.findUpperBound(mat[i], mid);
        return cnt;
        
    def median(self, mat):
    	# code here 
    	low = float('inf');
    	high = float('-inf');
    	numRows = len(mat);
    	numCols = len(mat[0]);
    	
    	for i in range(numRows):
    	    low = min(low, mat[i][0]);
    	    high = max(high, mat[i][numCols-1]);
    	
    	required = (numRows * numCols) // 2;
    	while low <= high:
    	    mid = (low + high) // 2;
    	    smallerReq = self.countSmallerRequired(mat, mid);
    	    if smallerReq > required:
    	        high = mid - 1;
    	    else:
    	        low = mid + 1;
    	        
    	return low;