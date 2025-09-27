class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(m) = O(2 * n + m)
    # Space Complexity: O(n + m)
    def mergeArrays(self, a, b):
        # code here
        i = 0;
        j = 0;
        temp = [];
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                temp.append(a[i]);
                i += 1;
            else:
                temp.append(b[j]);
                j += 1;

        if i < len(a):
            while i < len(a):
                temp.append(a[i]);
                i += 1;
        elif j < len(b):
            while j < len(b):
                temp.append(b[j]);
                j += 1;
                
        for k in range(len(a)):
            a[k] = temp[k];
        
        startIndex = len(a);
        for l in range(len(b)):
            b[l] = temp[startIndex]
            startIndex += 1;
            
        
        
        
        
