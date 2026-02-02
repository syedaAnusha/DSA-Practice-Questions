class Solution:
    # Optimal Approach
    # Time Complexity:O(nlogn)
    # Space Complexity:O(1)
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i];
        
    def getPartitionIndex(self, st, low, high):
        pivot = st[low];
        i = low;
        j = high;
        while i < j:
            while i <= high and st[i] <= pivot:
                i += 1;
            while j >= low and st[j] > pivot:
                j -= 1;
            if i < j:
                self.swap(st, i, j);
        self.swap(st, low, j);
        return j;
            
    def helperSortStack(self, low, high, st):
        if low < high:
            partitionIndex = self.getPartitionIndex(st, low, high);
            self.helperSortStack(low, partitionIndex-1, st);
            self.helperSortStack(partitionIndex+1, high, st)
        
    def sortStack(self, st):
        # code here 
        low = 0;
        high = len(st)-1;
        return self.helperSortStack(low, high, st);
