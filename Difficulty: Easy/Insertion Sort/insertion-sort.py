class Solution:
    # Time Complexity:
    # Worst & Avg. Case -> O(n^2)
    # Best Case -> O(n)
    # Space Complexity: O(1)
    
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def insertionSortArr(self, arr, i):
        if i == len(arr):
            return;
            
        j = i;
        while j > 0 and arr[j] < arr[j-1]:
            self.swap(arr, j, j-1);
            j -= 1;
            
        self.insertionSortArr(arr, i+1);
        
    def insertionSort(self, arr):
        # code here
        self.insertionSortArr(arr, 0);
        return arr;