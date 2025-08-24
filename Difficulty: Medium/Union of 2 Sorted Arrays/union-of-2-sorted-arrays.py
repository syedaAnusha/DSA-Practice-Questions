class Solution:
    # Time Complexity : O(a) + O(b) + O(a+b)
    # Space Complexity : O(a+b) -> for set{} + O(a+b) -> for returning union[] 
    def findUnion(self, a, b):
        # code here 
        uniqueElements = set();
        union = [];
        for i in range(len(a)):
            uniqueElements.add(a[i]);
        
        for j in range(len(b)):
            uniqueElements.add(b[j]);
        
        union = sorted(list(uniqueElements));
        return union;
            
        
        