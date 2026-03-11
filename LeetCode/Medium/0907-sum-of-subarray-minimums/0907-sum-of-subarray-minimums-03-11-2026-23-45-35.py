class Solution:
    # Optimal Approach
    # Time Complexity: O(5n)
    # Space Complexity: O(5n)
    MODULO = 10**9 + 7;
    def findPse(self, arr):
        psee = [];
        stack  = [];
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop();
            if not stack:
                psee.append(-1);
            else:
                psee.append(stack[-1]);
            stack.append(i);
        return psee;

    def findNse(self, arr):
        nse = [];
        stack  = [];
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop();
            if not stack:
                nse.append(len(arr));
            else:
                nse.append(stack[-1]);
            stack.append(i);
        return nse[::-1];

    def sumSubarrayMins(self, arr: List[int]) -> int:
        total = 0;
        nse = self.findNse(arr);
        pse = self.findPse(arr);
        for i in range(len(arr)):
            right = nse[i] - i;
            left = i - pse[i];
            total += (((right * left * arr[i]) % self.MODULO));
        return total % self.MODULO;