#User function Template for python3
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        # Time Complexity: O(n) + O(n) = O(2n)
        # Space Complexity: O(n) 
        d = d % len(arr);
        temp = arr[0:d];
        
        for i in range(d, len(arr)):
            arr[i-d] = arr[i];
        
        index = 0;
        N = len(arr)-d;
        for j in range(N, len(arr)):
            arr[j] = temp[index];
            index += 1;
        
            
            
        