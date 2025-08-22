#User function Template for python3
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def rotate(self, arr):
        for i in range(len(arr)-1,0,-1):
            self.swap(arr, i, i-1);
    
