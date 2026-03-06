class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arrOfnextGreaterElements = [];
        N = len(nums);
        for i in range(N):
            for j in range(i+1, i+N+1):
                ind = j % N;
                if nums[ind] > nums[i]:
                    arrOfnextGreaterElements.append(nums[ind]);
                    break;
            if nums[ind] == nums[i]:
                arrOfnextGreaterElements.append(-1);
        return arrOfnextGreaterElements;       