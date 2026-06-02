class Solution:
    # Optimal Approach
    # Time Complexity: O(n/2) = O(n)
    # Space Complexity: O(1)
    def checkForMaxHeap(self, arr, index, N):
        flag = True;
        while flag:
            largest = index;
            left = 2*index+1;
            right = 2*index+2;
            
            if left < N and arr[left] > arr[largest]:
                largest = left;
            if right < N and arr[right] > arr[largest]:
                largest = right;
            
            if largest != index:
                flag = False;
            else:
                break;
        return flag;
                
        
    def isMaxHeap(self, arr):
        # code here
        N = len(arr);
        nonLeafNodeIndex = N//2 - 1;
        for i in range(nonLeafNodeIndex, -1, -1):
            if self.checkForMaxHeap(arr, i, N):
                continue;
            return False;
        return True;