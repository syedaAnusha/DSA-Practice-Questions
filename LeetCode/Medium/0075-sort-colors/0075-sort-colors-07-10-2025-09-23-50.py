class Solution(object):
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];

    def partition(self, arr, low, high):
        pivot = arr[low];
        i = low;
        j = high;
        while i < j:
            while arr[i] <= pivot and i <= high-1:
                i+=1;
            while arr[j] > pivot and j >= low+1:
                j-=1;
            if i < j:
                self.swap(arr, i, j);
        self.swap(arr, low, j)
        return j;
    def quickSort(self, arr, low, high):
        if low <= high:
            partitionIndex = self.partition(arr, low, high);
            self.quickSort(arr, low, partitionIndex-1);
            self.quickSort(arr, partitionIndex+1, high);

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums)-1);
        