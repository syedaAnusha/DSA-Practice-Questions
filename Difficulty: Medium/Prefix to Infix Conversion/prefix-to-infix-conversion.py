#User function Template for python3

class Solution:
    # Time Complexity: O(n) + O(n^2), if str concatenation is deep, otherwise O(n)
    # Space Complexity: O(n)
    def makeExpressionFrom(self, operator1, operator2, operand):
        return '(' + operator1 + operand + operator2 + ')';
        
    def preToInfix(self, pre_exp):
        # Code here
        stack = [];
        
        for ch in pre_exp[::-1]:
            if ch.isalnum():
                stack.append(ch);
            else:
                operator1 = stack.pop();
                operator2 = stack.pop();
                expression = self.makeExpressionFrom(operator1, operator2, ch);
                stack.append(expression);
                
        return stack[-1];