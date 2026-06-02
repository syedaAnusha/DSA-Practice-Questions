class Solution:
    # Optimal Approach
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(log n)
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
    
    def findLargestNodeIndex(self, arr, index, size):
        largest = index;
        left = 2*index+1;
        right = 2*index+2;
        
        if left < size and arr[left] > arr[largest]:
            largest = left;
        if right < size and arr[right] > arr[largest]:
            largest = right;
        
        return largest;
        
        
    def heapify(self, arr, index, size):
        largest = index;
        left = 2*index+1;
        right = 2*index+2;
        
        if left < size and arr[left] > arr[largest]:
            largest = left;
        if right < size and arr[right] > arr[largest]:
            largest = right;
        
        if largest != index:
            self.swap(arr, index, largest);
            self.heapify(arr, largest, size);
            
    def convertToMaxHeap(self, arr):
        N = len(arr);
        startNodeIndex = (N//2)-1;
        i = startNodeIndex;
        while i >= 0:
            self.heapify(arr, i, N);
            i -= 1;
    
    def sortArray(self, arr):
        i = len(arr)-1;
        while i > 0:
            self.swap(arr, i, 0);
            self.heapify(arr, 0, i);
            i -= 1;
            
        
    def heapSort(self, arr):
        #code here
        self.convertToMaxHeap(arr);
        self.sortArray(arr);
        return arr;
        
        