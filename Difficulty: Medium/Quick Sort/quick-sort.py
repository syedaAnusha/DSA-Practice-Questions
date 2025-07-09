class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low <= high:
            partitionIndex = self.partition(arr, low, high);
            self.quickSort(arr,low,partitionIndex-1);
            self.quickSort(arr,partitionIndex+1, high);
            
            
    
    def partition(self,arr,low,high):
        # code here
        pivot = arr[high];
        i = low;
        j = high;
        while i < j:
            while(arr[i] < pivot and i <= high-1):
                i += 1;
            while(arr[j] >= pivot and j >= low):
                j -= 1;
            if i < j:
                arr[i], arr[j] = arr[j], arr[i];
        arr[high], arr[i] = arr[i], arr[high];
        return i;
    