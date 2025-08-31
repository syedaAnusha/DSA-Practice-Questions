class Solution: 
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    self.swap(arr, i, j);
                
        