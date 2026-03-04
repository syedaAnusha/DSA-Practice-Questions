class Solution:
    # Optimal Aoproach
    # Time Complexity: O(2n) + O(n)
    # Space Complexity: O(n) + O(n)
    
    def nextLargerElement(self, arr):
        # code here
        ans = [];
        stack = [];
        
        for i in range(len(arr)-1, -1, -1):
            if not stack:
                ans.append(-1);
                stack.append(arr[i]);
            elif stack and arr[i] < stack[-1]:
                ans.append(stack[-1]);
                stack.append(arr[i]);
            else:
                while stack and arr[i] >= stack[-1]:
                    stack.pop();
                if stack:
                    ans.append(stack[-1]);
                    stack.append(arr[i]);
                else:
                    ans.append(-1);
                    stack.append(arr[i]);
        return ans[::-1];