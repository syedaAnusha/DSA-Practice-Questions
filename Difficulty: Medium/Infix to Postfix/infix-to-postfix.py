class Solution:
    # Time Complexity: O(n) + O(n) , where O(n) for outer and O(n) for inner loop
    # Space Complexity: O(n) + O(n) where O(n) for stack and O(n) for postfixExp variable
    def getPriorityOfAn(self, operator):
        if operator == '^':
            return 3;
        elif operator == '*' or operator == '/':
            return 2;
        elif operator == '+' or operator == '-':
            return 1;
        else:
            return -1;
            
    def isNotRightAssociative(self, operator):
        if operator == '^':
            return False;
        return True;
            
    def infixtoPostfix(self, s):
        #code here
        postfixExp = [];
        stack = [];

        for i in range(len(s)):
            if s[i].isalnum():
                postfixExp.append(s[i]);
                
            elif s[i] == '(':
                stack.append(s[i]);
                
            elif s[i] == ')':
                while stack and stack[-1] != '(':
                    postfixExp.append(stack.pop());
                stack.pop();
                
            else:
                while stack and self.getPriorityOfAn(s[i]) <= self.getPriorityOfAn(stack[-1]) and self.isNotRightAssociative(s[i]):
                    postfixExp.append(stack.pop());
                stack.append(s[i]);
            
        while stack:
            postfixExp.append(stack.pop());
        
        return "".join(postfixExp);