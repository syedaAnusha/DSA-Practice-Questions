class Solution:
    # T.C = O(n^2) - Worst Case & Avg.Case O(n): Best Case
    # S.C = O(1)
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def bubbleSort(self,arr):
        # code here
        i = len(arr)-1;
        isMaxFound = False;
        while i > 0:
            j = 0;
            while j < i:
                if arr[i] < arr[j]:
                    self.swap(arr, i, j);
                    isMaxFound = True;
                j += 1
            i -= 1
                
        
       
        