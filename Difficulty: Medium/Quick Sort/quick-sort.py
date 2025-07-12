import random
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low <= high:
            partitionIndex = self.partition(arr, low, high);
            self.quickSort(arr,low, partitionIndex-1);
            self.quickSort(arr,partitionIndex+1, high);
            
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def randomPartition(self, arr, low, high):
        random_integer = random.randint(low, high);
        self.swap(arr,random_integer, low);
        return self.partition(arr,low,random_integer)
        
    def partition(self,arr,low,high):
        # code here
        pivot = arr[low];
        i = low;
        j = high;
        while i < j:
            while arr[i] <= pivot and i <= high-1:
                i += 1;
            while arr[j] > pivot and j >= low+1:
                j -= 1;
            if i < j:
                self.swap(arr, i, j);
        self.swap(arr, low, j);
        return j;
                
    