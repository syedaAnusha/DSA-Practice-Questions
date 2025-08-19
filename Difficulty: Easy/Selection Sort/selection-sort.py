class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)-1):
            minValueIndex = i;
            for j in range(i, len(arr)):
                if arr[j] < arr[minValueIndex]:
                    minValueIndex = j;
            self.swap(arr, minValueIndex, i);
        
        return arr;           