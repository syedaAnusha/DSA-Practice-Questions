#User function Template for python3

class Solution:
    # Time Complexity: O(n) + O(n^2)
    # Space Complexity: O(n)
    def preToPost(self, pre_exp):
        # Code here
        stack = [];
        
        for ch in pre_exp[::-1]:
            if ch.isalnum():
                stack.append(ch);
            else:
                top1 = stack.pop();
                top2 = stack.pop();
                expression =  top1 + top2 + ch;
                stack.append(expression);
                
        return stack[-1];