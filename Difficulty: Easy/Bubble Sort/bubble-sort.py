class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def bubbleSort(self,arr):
        # code here
        i = len(arr)-1;
        j = 0;
        while i >= 0:
            didSwap = 0;
            for j in range(0, i):       
                if arr[j] > arr[j+1]:
                    self.swap(arr,j, j+1);
                    didSwap = 1;
            if didSwap == 0:
                break;
            i -= 1;
        return arr;