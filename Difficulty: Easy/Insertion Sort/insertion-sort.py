class Solution:
    # Time Complexity:
    # Worst & Avg. Case -> O(n^2)
    # Best Case -> O(n)
    # Space Complexity: O(1)
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
    
    def insertionSort(self, arr):
        # code here
        for i in range(len(arr)):
            j = i;
            while j > 0:
                if arr[j-1] > arr[j]:
                    self.swap(arr, j-1, j);
                j -= 1;
                    
                    
        