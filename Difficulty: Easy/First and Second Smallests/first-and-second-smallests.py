class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        smallest = arr[0];
        secSmallest = float('inf');
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                secSmallest = smallest;
                smallest = arr[i];
            elif arr[i] < secSmallest and arr[i] > smallest:
                secSmallest = arr[i];
        
        if secSmallest == float('inf'):
            return [-1];
        else:
            return [smallest, secSmallest];
                
                
                
        
