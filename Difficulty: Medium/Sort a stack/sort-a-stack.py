class Solution:
    # Brute Force Approach
    # Time Complexity:O(2n) + O(nlogn)
    # Space Complexity:O(n)
    def sortStack(self, st):
        # code here 
        arr = [];
        i = 0;
        while i < len(st):
            arr.append(st[i]);
            i += 1;
        arr.sort();
        i = 0;
        while i < len(arr):
            st[i] = arr[i];
            i += 1;
        return st;