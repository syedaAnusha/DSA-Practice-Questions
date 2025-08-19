class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def bubbleSort(self,arr):
        # code here
        i = len(arr)-1;
        j = 0;
        while i >= 0:
            minValIndex = 0;
            for j in range(0, i+1):       
                if arr[j] > arr[minValIndex]:
                    minValIndex = j;
            self.swap(arr,minValIndex, i);
            i -= 1;
        return arr;