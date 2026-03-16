class Solution:
    # Brute Force Approach
    # Time Complexity: O(5n) + O(5n)
    # Space Complexity: O(10n)
    MODULO = 10**9 + 7;
    def findPge(self, arr):
        pgee = [];
        stack  = [];
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop();
            if not stack:
                pgee.append(-1);
            else:
                pgee.append(stack[-1]);
            stack.append(i);
        return pgee;

    def findNge(self, arr):
        nge = [];
        stack  = [];
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop();
            if not stack:
                nge.append(len(arr));
            else:
                nge.append(stack[-1]);
            stack.append(i);
        return nge[::-1];

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

    def subArraySumMins(self, arr):
        total = 0;
        nse = self.findNse(arr);
        pse = self.findPse(arr);
        for i in range(len(arr)):
            right = nse[i] - i;
            left = i - pse[i];
            total += (((right * left * arr[i])));
        return total;

    def subArraySumMaxs(self, arr):
        total = 0;
        nge = self.findNge(arr);
        pge = self.findPge(arr);
        for i in range(len(arr)):
            right = nge[i] - i;
            left = i - pge[i];
            total += (((right * left * arr[i])));
        return total;

    def subArrayRanges(self, nums: List[int]) -> int:
        sumOfMin = self.subArraySumMins(nums);
        sumOfMax = self.subArraySumMaxs(nums);
        return sumOfMax-sumOfMin;
