class Solution:
    def largest(self, arr):
        # code here
        largestValue = float('-inf');
        for i in range(len(arr)):
            if arr[i] > largestValue:
                largestValue = arr[i];
        return largestValue;
        
