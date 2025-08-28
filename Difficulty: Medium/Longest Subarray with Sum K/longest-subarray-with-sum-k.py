class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    def longestSubarray(self, arr, k):  
        # code here
        maxLen = 0;
        Sum = 0;
        hashSet = {};
        for i in range(len(arr)):
            Sum += arr[i];
            
            if Sum not in hashSet:
                hashSet[Sum] = i;
            
            if Sum == k:
                maxLen = max(maxLen, i+1);
            
            rem = Sum - k;
            if rem in hashSet:
                maxLen = max(maxLen, i-hashSet[rem]);
        return maxLen;
        
            
    
