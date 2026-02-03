class Solution:
    # Brute Approach
    # Time Complexity:O(n^2)
    # Space Complexity: O(n)
    def helperReverseStack(self, stack, curVal):
        if not stack:
            stack.append(curVal);
            return stack;
            
        val = stack.pop();
        self.helperReverseStack(stack, curVal);
        stack.append(val);
        
        
    def reverseStack(self, st):
        # code here
        if st:
            curVal = st.pop();
            self.reverseStack(st);
            self.helperReverseStack(st, curVal);
