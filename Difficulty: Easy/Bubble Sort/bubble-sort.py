class Solution:
    # T.C = O(n^2) - Worst Case & Avg.Case O(n): Best Case
    # S.C = O(1)
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
    
    def bubbleSortArr(self, arr, i, didSwap):
        if i < 0:
            return;
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                self.swap(arr, j, j+1);
                didSwap = True;
                
        if not didSwap:
            return;
        self.bubbleSortArr(arr, i-1, didSwap);
        
    def bubbleSort(self,arr):
        # code here
        self.bubbleSortArr(arr, len(arr)-1, False);
        return arr;
        