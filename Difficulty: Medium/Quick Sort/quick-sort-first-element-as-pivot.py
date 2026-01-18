class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def quickSort(self, arr, low, high):
        #code here 
        if low < high:
            partitionIndex = self.partition(arr, low, high);
            self.quickSort(arr, low, partitionIndex-1);
            self.quickSort(arr, partitionIndex+1, high);
            

    def partition(self, arr, low, high):
        #code here
        pivot = arr[low];
        i = low;
        j = high;
        while i < j:
            while i<= high and arr[i] <= pivot:
                i += 1;
            while j >= low and arr[j] > pivot:
                j -= 1;
            
            if i < j:
                self.swap(arr, i, j);
        self.swap(arr, low, j)
        return j;
