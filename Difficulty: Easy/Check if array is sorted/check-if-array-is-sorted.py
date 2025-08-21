class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        i = 1;
        while i < len(arr):
            if arr[i] >= arr[i-1]:
                i += 1;
                continue;
            else:
                return False;
            
        return True;
                