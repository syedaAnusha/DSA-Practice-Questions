class Solution:
    # Optimal Approach
    # Time Complexity: O(n+m) e.g n = [1,2,3,4] m = [1,2,3,4]
    # Space Complexity: O(min(n,m))
    
    def intersection(self, arr1, arr2):
        #code here
        intersection = [];
        i = 0;
        j = 0;
        lenArr1 = len(arr1);
        lenArr2 = len(arr2);
        
        while i < lenArr1 and j < lenArr2:
            if arr1[i] < arr2[j]:
                i += 1;
            elif arr2[j] < arr1[i]:
                j += 1;
            else:
                if len(intersection) == 0 or intersection[-1] != arr1[i]:
                    intersection.append(arr1[i]);
                i += 1;
        
        return intersection;
        
    
