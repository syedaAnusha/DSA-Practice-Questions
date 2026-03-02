#User function Template for python3

class Solution:
    # Time Complexity: O(n) + O(n) because string concatenation takes time as strings are immutable
    # Space Complexity: O(n)
    def addBracketsToExp(self, operator1, operator2, operand):
        return '('+ operator1 + operand + operator2 + ')';
        
    def postToInfix(self, postfix):
        # Code here
        stack = [];
        
        for ch in postfix:
            if ch.isalnum():
                stack.append(ch);
                
            else:
                operator2 = stack.pop();
                operator1 = stack.pop();
                exp = self.addBracketsToExp(operator1, operator2, ch);
                stack.append(exp);
                
        return stack[-1];