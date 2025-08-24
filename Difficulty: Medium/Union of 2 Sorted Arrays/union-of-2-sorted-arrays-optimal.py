class Solution:
    # Optimal Approach
    # Time Complexity : O(a+b)
    # Space Complexity : O(a+b)
    def findUnion(self, a, b):
        # code here 
        union = [];
        i = 0; 
        j = 0;
    
        while i < len(a) and j < len(b):
            value = min(a[i], b[j]);
            if len(union) == 0 or union[-1] != value:
                union.append(value);
            
            if a[i] == value:
                i += 1;
            else:
                j += 1;
    
        if j < len(b):
            while j < len(b):
                if union[-1] != b[j]:
                    union.append(b[j]);
                j += 1;
        else:
            while i < len(a):
                if union[-1] != a[i]:
                    union.append(a[i]);
                i += 1;
                
        return union;
            
        
        
