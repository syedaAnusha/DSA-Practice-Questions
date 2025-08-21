class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        largest = arr[0];
        secLargest = -1; # set to -1, if all numbers are positive. else, set to -inf 
        for i in range(1, len(arr)):
            if arr[i] > largest:
                secLargest = largest;
                largest = arr[i];
            elif arr[i] != largest and arr[i] > secLargest:
                secLargest = arr[i];
        return secLargest;
           
                
            
            
