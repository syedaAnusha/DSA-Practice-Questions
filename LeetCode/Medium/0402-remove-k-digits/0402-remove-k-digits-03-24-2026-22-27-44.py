class Solution:
    # Optimal Greedy Approach
    # Time Complexity: O(n) + O(k) + O(n) + O(n)
    # Space Complexity: O(n) + O(n)
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [];
        res = [];
        if k == len(num):
            return "0";

        for i in range(len(num)):
            while stack and k > 0 and int(stack[-1]) > int(num[i]):
                stack.pop();
                k -= 1;
            stack.append(num[i]);
        

        while stack and k > 0:
            stack.pop();
            k -= 1;
        
        if not stack:
            return "0";
           
        while stack:
            res.append(stack.pop());
            
        while res and res[-1] == '0':
            res.pop();
        
        if not res:
            return '0';
        return "".join(res[::-1]);