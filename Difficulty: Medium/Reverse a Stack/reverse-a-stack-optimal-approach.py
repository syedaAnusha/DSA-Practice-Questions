class Solution:
    # Optimal Approach
    # Time Complexity:O(n)
    # Space Complexity: O(1)
    def swapValues(self, i, j, st):
        st[i], st[j] =  st[j], st[i];
        
    def reverseStack(self, st):
        # code here
        start = 0;
        end = len(st)-1;
        while start < end:
            self.swapValues(start, end, st);
            start += 1;
            end -=1;
        return st;
