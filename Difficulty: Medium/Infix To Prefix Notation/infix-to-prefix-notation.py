class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def checkPrecedenceOf(self, operator):
        if operator == '^':
            return 3
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '+' or operator == '-':
            return 1
        else:
            return -1
    
    def swap(self, i, j, exp):
        exp[i], exp[j] = exp[j], exp[i]
    
    def reverseExpression(self, expression):
        expList = list(expression)
        i = 0
        j = len(expList) - 1

        while i < j:
            # swap brackets first (safer logic)
            if expList[i] == '(':
                expList[i] = ')'
            elif expList[i] == ')':
                expList[i] = '('

            if expList[j] == '(':
                expList[j] = ')'
            elif expList[j] == ')':
                expList[j] = '('

            self.swap(i, j, expList)
            i += 1
            j -= 1
        
        if expList[i] == '(' and expression[i] == expList[i]:
            expList[i] = ')';
        elif expList[i] == ')' and expression[i] == expList[i]:
            expList[i] = '(';
            
        return "".join(expList)
        
    def infixToPrefix(self, s):
        stack = []
        expression = []

        newStr = self.reverseExpression(s)

        for ch in newStr:
            # Operand
            if ch.isalnum():
                expression.append(ch)

            # Opening bracket
            elif ch == '(':
                stack.append(ch)

            # Closing bracket
            elif ch == ')':
                while stack and stack[-1] != '(':
                    expression.append(stack.pop())

                # SAFE POP (fixes your runtime error)
                if stack and stack[-1] == '(':
                    stack.pop()

            # Operator
            else:
                if ch == '^':
                    while stack and self.checkPrecedenceOf(ch) == self.checkPrecedenceOf(stack[-1]):
                        expression.append(stack[-1]);
                        stack.pop()
                else:
                    while stack and self.checkPrecedenceOf(ch) < self.checkPrecedenceOf(stack[-1]):
                        expression.append(stack[-1]);
                        stack.pop()
                stack.append(ch)

        # Pop remaining operators
        while stack:
            expression.append(stack.pop())

        # Reverse to get prefix
        return self.reverseExpression("".join(expression))