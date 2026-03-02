#User function Template for python3

class Solution:
    # Time Complexity: O(n) +  O(n)
    # Space Complexity: O(n)
    def postToPre(self, post_exp):
        # Code here
        stack = [];
        
        for ch in post_exp:
            if ch.isalnum():
                stack.append(ch);
            else:
                top1 = stack.pop();
                top2 = stack.pop();
                expression = ch + top2 + top1;
                stack.append(expression);
                
        return stack[-1];