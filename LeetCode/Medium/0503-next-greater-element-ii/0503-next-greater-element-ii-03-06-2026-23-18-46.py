class Solution:
    # Optimal Approach
    # Time Complexity: O(2n) + O(2n) + O(n)
    # Space Complexity: O(2n) + O(n)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arrOfnextGreaterElements = [];
        stack = [];
        N = len(nums);
        for i in range(2*N-1,-1,-1):
            while stack and nums[i%N] >= stack[-1]:
                stack.pop();
            if i < N:
                if not stack:
                    arrOfnextGreaterElements.append(-1);
                else:
                    arrOfnextGreaterElements.append(stack[-1]);
            stack.append(nums[i%N]); 
        return arrOfnextGreaterElements[::-1];       