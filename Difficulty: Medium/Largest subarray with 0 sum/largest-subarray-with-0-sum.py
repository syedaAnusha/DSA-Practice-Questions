class Solution:
    # Optimal Approach
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def maxLength(self, arr):
        # code here
        maxi = 0;
        Sum = 0;
        hashMap = dict();
        for i in range(len(arr)):
            Sum += arr[i];
            if Sum == 0:
                maxi = i + 1;
            else:
                if Sum in hashMap:
                    maxi = max(maxi, i-hashMap[Sum]);
                else:
                    hashMap[Sum] = i;
        
        return maxi;